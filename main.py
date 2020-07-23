import cv2
import controls

WIDTH = 640
HEIGHT = 480

constraintLeft = (WIDTH // 3) 
constraintRight = constraintLeft * 2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
# Better FPS and processing
cap.set(3, WIDTH)
cap.set(4, HEIGHT)

while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.line(frame, (constraintLeft, 0), (constraintLeft, 480), (255,255,255), 1)
    frame = cv2.line(frame, (constraintRight, 0), (constraintRight, 480), (255,255,255), 1)

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)
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
            controls.left()
        elif centerX > constraintRight:
            controls.right()
        else:
            controls.fire()

    cv2.imshow('Video Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()