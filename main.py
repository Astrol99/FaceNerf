import face_recognition
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Better FPS and processing
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret,frame = cap.read()

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img1', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()