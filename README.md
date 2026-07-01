# i2i-Academy-Computer_Vision-3
Real-time hand tracking and finger counting project built with Python, OpenCV, and the modern MediaPipe Tasks API.
# Real-Time Hand Tracking & Finger Counter

--This repository contains a real-time computer vision application that detects human hands and counts open fingers using a live webcam feed. This project was built as part of the i2i Academy Computer Vision module.

## Project Description:
The application captures video frames from the webcam, processes them to find hand landmarks, and calculates the number of extended fingers. The counting logic compares the vertical positions (Y-coordinates) of the fingertips with their respective lower joints to determine if a finger is open or closed.

## Features:
* **Real-Time Tracking:** High-speed hand and landmark detection.
* **Dynamic Finger Counting:** Real-time counter displayed directly on the screen.
* **Multi-Hand Support:** Detects and processes up to 2 hands simultaneously.
* **Modern Architecture:** Bypasses deprecated legacy modules for future-proof stability.

## Tech Stack & Requirements:
* **Python 3.12+**
* **OpenCV** (for webcam control and rendering)
* **MediaPipe Tasks API** (for advanced hand landmarker models)

## The Technical Challenge & Resolution
During development, we encountered a critical `AttributeError` caused by the deprecated `mediapipe.solutions` module found in older documentation. Since Google removed this legacy framework in newer versions, we successfully refactored the entire project to utilize the modern **MediaPipe Tasks API** (`HandLandmarker`). Additionally, to prevent dependency conflicts, we created a custom drawing loop using pure OpenCV (`cv2.circle`) to manually render the 21 hand joints flawlessly.

## How to Run the Project:

1. **Open your terminal inside the project directory:**
   ```bash
   cd i2i-Academy-ComputerVision-3
