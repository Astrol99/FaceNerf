from cv2 import cv2
import controller

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FPS, 60)

HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

constraintLeft = WIDTH // 3
constraintRight = constraintLeft * 2

while cap.isOpened():
    ret, frame = cap.read()

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = cv2.line(frame, (constraintLeft, 0), (constraintLeft, HEIGHT), (255,255,255), 1)
    frame = cv2.line(frame, (constraintRight, 0), (constraintRight, HEIGHT), (255,255,255), 1)

    faces = faceCascade.detectMultiScale(frame, 1.3, 5)
    faceClosest = { "area": 0 }

    for (x, y, w, h) in faces:
        x2, y2 = x+w, y+h
        faceArea = w * h

        # Draw green (signal for irrelevant faces) rectangles around all faces in frame as default
        frame = cv2.rectangle(frame, (x,y), (x2,y2), (0,255,0), 1)
        
        # Attempt to sort all faces in frame by closest one (biggest one)
        if faceArea > faceClosest["area"]:
            faceClosest["area"] = faceArea
            faceClosest["xy"] = (x,y)
            faceClosest["xy2"] = (x2, y2)
            faceClosest["wh"] = (w,h)

    # If faces do exist
    if faces != ():
        # Draw red (signal for priority face) rectangle for priority target face
        frame = cv2.rectangle(frame, faceClosest["xy"], faceClosest["xy2"], (0,0,255), 1) 

        centerX = faceClosest["xy"][0] + (faceClosest["wh"][0]//2)
        centerY = faceClosest["xy"][1] + (faceClosest["wh"][1]//2)

        # Draw center of target face
        frame = cv2.line(frame, (centerX, centerY), (centerX, centerY), (0,0,255), 2)

        # Detect if face is within constraints 
        if centerX < constraintLeft:
            controller.left()
        elif centerX > constraintRight:
            controller.right()
        else:
            controller.fire()
        
    cv2.imshow('FaceNerf', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()