# Codeversity_SensorSurge
Official Repo for Codeversity by Team SensorSurge

---

# KrishiRakshak AI 🌾

KrishiRakshak AI is an edge-AI powered farm decision and risk support system designed to help Indian smallholder farmers make timely, data-driven agricultural decisions. The project focuses on reducing crop risk and uncertainty caused by climate variability, rising input costs, and limited access to reliable advisory services by converting real-time farm data into clear, actionable recommendations.

The system is built as a practical, low-cost Proof of Concept that combines hardware sensing, edge computing, and lightweight machine learning to deliver localized farm intelligence even in low-connectivity rural environments.

---

## Problem Motivation

Indian agriculture is dominated by small and marginal farmers who often rely on intuition or delayed information for critical decisions such as irrigation, sowing, and harvesting. Erratic monsoons, heat stress, and unpredictable weather patterns increase the risk of crop loss and income instability. Many existing digital solutions are cloud-dependent, data-heavy, or difficult to use for farmers with limited digital literacy.

KrishiRakshak AI addresses this gap by focusing on decision support rather than raw data display, while remaining affordable, accessible, and deployable at the field level.

---

## Solution Overview

KrishiRakshak AI deploys a low-cost sensor unit in the field to continuously monitor local environmental and soil conditions. The collected data is processed locally using a Raspberry Pi 5, enabling edge-based intelligence without continuous internet dependency.

The system combines agronomy-based rule logic for immediate alerts with a lightweight machine learning model trained on local micro-climate data to predict short-term crop stress and irrigation risk. Instead of presenting raw sensor values, the system provides context-aware recommendations that farmers can easily understand and act upon.

---

## Key Features

* Real-time monitoring of soil moisture, temperature, humidity, and light intensity
* Edge-based processing for offline operation, low latency, and data privacy
* Hybrid intelligence using agronomic rules and machine learning
* Short-term prediction of crop stress and irrigation risk
* Localized weather awareness for rainfall and heat stress conditions
* Simple farmer-friendly dashboard
* Optional voice-based alerts for low digital literacy users
* Modular design for future expansion

---

## System Architecture

1. Field sensors capture real-time soil and environmental data
2. Embedded controller transmits data to the Raspberry Pi 5
3. Edge AI engine performs risk assessment and prediction
4. Decision logic generates actionable advisories
5. Dashboard and alerts present recommendations to the farmer

All core processing is performed locally to ensure reliability in rural and low-connectivity environments.

---

## Government Scheme Awareness

This module helps farmers stay informed about active and relevant government agricultural schemes. It provides simplified information on subsidies, MSP announcements, crop insurance programs, and seasonal support schemes.

The feature highlights scheme eligibility, key benefits, and important deadlines in a farmer-friendly format. It integrates with KrishiRakshak AI advisories to align risk alerts with available government support.

Designed for low-bandwidth environments, this module supports future expansion into personalized recommendations, regional language support, and integration with official government data sources.

---

## Technology Stack

Hardware
Soil moisture sensor
Temperature and humidity sensor
Light intensity sensor

Edge Device
Raspberry Pi 5

Embedded Controller
ESP32 or equivalent microcontroller

Software
Python
Lightweight machine learning models
Rule-based decision logic

Interface
Web dashboard
Optional voice-based alerts

---

## Why Edge AI

KrishiRakshak AI processes data locally at the edge instead of relying on cloud infrastructure. This reduces latency, lowers operational costs, improves data privacy, and ensures consistent performance in areas with unreliable or no internet connectivity. Local learning also allows the system to adapt to farm-specific micro-climate conditions over time.

---

## Social Impact

The project aims to empower Indian smallholder farmers by providing timely, localized, and explainable agricultural advisories. By improving irrigation efficiency, reducing input wastage, and offering early risk warnings, KrishiRakshak AI helps improve livelihood stability and resilience against climate uncertainty. The low-tech design ensures inclusivity for farmers with limited digital literacy.

---

## Business Viability

KrishiRakshak AI is designed as a low-cost and scalable AgriTech solution aligned with the economic realities of smallholder farmers. The hardware involves a one-time affordable cost, while edge-based processing reduces recurring operational expenses.

The software platform can follow a freemium or subscription-based model, where basic advisories are offered at minimal or no cost, and advanced predictive features are available through low seasonal or monthly plans. The solution also enables B2B and B2G adoption through partnerships with farmer producer organizations, agribusinesses, crop insurance providers, and government agencies.

---

## Scalability and Future Scope

The current Proof of Concept focuses on micro-climate monitoring and irrigation risk prediction. The modular architecture allows future integration of pest and disease risk alerts, market price and mandi intelligence, crop insurance awareness, and government scheme notifications, enabling a unified agricultural decision support platform.

---

## Project Status

KrishiRakshak AI is developed as a working Proof of Concept for a hackathon and demonstrates the feasibility of deploying edge-AI based agricultural decision support systems in real-world farm environments.

---

## Team

This project was built with a strong focus on practical deployment, rapid prototyping, and solving real agricultural challenges faced by Indian smallholder farmers.

