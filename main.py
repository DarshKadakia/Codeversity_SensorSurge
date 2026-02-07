from flask import Flask, Response
import cv2
import numpy as np
import time

ESP32_STREAM_URL = "http://192.168.1.60/stream"

app = Flask(__name__)

def get_capture():
    cap = cv2.VideoCapture(ESP32_STREAM_URL)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    return cap

def generate_frames():
    cap = get_capture()

    while True:
        if not cap.isOpened():
            print("[WARN] Reconnecting to ESP32 stream...")
            cap.release()
            time.sleep(1)
            cap = get_capture()
            continue

        ret, frame = cap.read()

        if not ret:
            print("[WARN] Frame lost, reconnecting...")
            cap.release()
            time.sleep(0.5)
            cap = get_capture()
            continue

        frame = cv2.resize(frame, (640, 480))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Green detection
        lower_green = np.array([35, 40, 40])
        upper_green = np.array([85, 255, 255])
        green_mask = cv2.inRange(hsv, lower_green, upper_green)

        kernel = np.ones((5, 5), np.uint8)
        green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)
        green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(
            green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        leaf_mask = np.zeros_like(green_mask)

        if contours:
            largest = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest) > 3000:
                cv2.drawContours(leaf_mask, [largest], -1, 255, -1)
                cv2.drawContours(frame, [largest], -1, (255, 0, 0), 2)

        leaf_pixels = cv2.countNonZero(leaf_mask)

        if leaf_pixels > 0:
            green_pixels = cv2.countNonZero(
                cv2.bitwise_and(green_mask, green_mask, mask=leaf_mask)
            )
            green_ratio = green_pixels / leaf_pixels
        else:
            green_ratio = 0.0

        if green_ratio >= 0.55:
            status = "HEALTHY"
            color = (0, 255, 0)
        else:
            status = "UNHEALTHY"
            color = (0, 0, 255)

        cv2.putText(frame, f"Status: {status}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, color, 3)
        cv2.putText(frame, f"Green Ratio: {green_ratio:.2f}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" +
               frame_bytes +
               b"\r\n")

@app.route("/")
def index():
    return """
    <html>
      <body style="text-align:center;">
        <h2>Leaf Health Monitor</h2>
        <img src="/video" width="720">
      </body>
    </html>
    """

@app.route("/video")
def video():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
