import cv2
import numpy as np

# Load Cascades
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
# Better FPS and processing
cap.set(3, 640)
cap.set(4, 480)

while cap.isOpened():
    ret, frame = cap.read()

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert frame to grayscale

    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)
    for (x, y, w, h) in faces:
        x2, y2 = x+w, y+h
        frame = cv2.rectangle(frame, (x,y), (x2, y2), (0,0,255), 1)

    cv2.imshow('Video Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()