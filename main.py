import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import urllib.request
import os

# 1. Download Google's official modern model file if it doesn't exist
model_path = "hand_landmarker.task"
if not os.path.exists(model_path):
    print("Downloading modern MediaPipe model file... Please wait.")
    model_url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"
    urllib.request.urlretrieve(model_url, model_path)
    print("Download complete successfully!")

# 2. Setup the modern MediaPipe Tasks API
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

# 3. Open the webcam
camera = cv2.VideoCapture(0)
print("Press 'q' to exit.")

while camera.isOpened():
    success, frame = camera.read()
    if not success:
        print("Failed to get frame from camera.")
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    detection_result = detector.detect(mp_image)

    # Check if any hand is detected
    if detection_result.hand_landmarks:
        for hand_landmarks in detection_result.hand_landmarks:
            
            # List to track which fingers are open
            opened_fingers = []

            # 4 Fingers logic (Index, Middle, Ring, Pinky)
            # Compare tip Y with PIP joint Y (smaller Y means higher on screen)
            
            # Index Finger (Tip: 8, PIP: 6)
            if hand_landmarks[8].y < hand_landmarks[6].y:
                opened_fingers.append(1)
                
            # Middle Finger (Tip: 12, PIP: 10)
            if hand_landmarks[12].y < hand_landmarks[10].y:
                opened_fingers.append(1)
                
            # Ring Finger (Tip: 16, PIP: 14)
            if hand_landmarks[16].y < hand_landmarks[14].y:
                opened_fingers.append(1)
                
            # Pinky Finger (Tip: 20, PIP: 18)
            if hand_landmarks[20].y < hand_landmarks[18].y:
                opened_fingers.append(1)

            # Thumb Finger logic (Tip: 4, IP: 3)
            # Thumbs move horizontally, so we compare X coordinates
            if hand_landmarks[4].x > hand_landmarks[3].x:
                opened_fingers.append(1)

            # Calculate total number of open fingers
            total_fingers = len(opened_fingers)

            # Draw green circles on each joint
            for landmark in hand_landmarks:
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            # Display the finger count text on the live screen
            cv2.putText(frame, f"Fingers: {total_fingers}", (50, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

    # Display the modern tracking window
    cv2.imshow("Modern Hand Tracking Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
detector.close()