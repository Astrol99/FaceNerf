import cv2
import controls

WIDTH = 640
HEIGHT = 480

restraintLeft = (WIDTH // 3) 
restraintRight = restraintLeft * 2

# Load Cascades
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
# Better FPS and processing
cap.set(3, WIDTH)
cap.set(4, HEIGHT)

while cap.isOpened():
    ret, frame = cap.read()

    #############
    frame = cv2.line(frame, (restraintLeft, 0), (restraintLeft, 480), (0,0,0), 1)
    frame = cv2.line(frame, (restraintRight, 0), (restraintRight, 480), (0,0,0), 1)
    #############

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)
    faceClosest = { "area": 0 }

    for (x, y, w, h) in faces:
        x2, y2 = x+w, y+h
        faceArea = w * h

        frame = cv2.rectangle(frame, (x,y), (x2,y2), (0,255,0), 1)
        
        # Attempt to sort all faces in frame by closest one (biggest one)
        if faceArea > faceClosest["area"]:
            faceClosest["area"] = faceArea
            faceClosest["xy"] = (x,y)
            faceClosest["xy2"] = (x2, y2)
            faceClosest["wh"] = (w,h)

    # If faces do exist
    if faces != ():
        frame = cv2.rectangle(frame, faceClosest["xy"], faceClosest["xy2"], (0,0,255), 1)

        centerX = faceClosest["xy"][0] + (faceClosest["wh"][0]//2)
        centerY = faceClosest["xy"][1] + (faceClosest["wh"][1]//2)

        frame = cv2.line(frame, (centerX, centerY), (centerX, centerY), (0,0,255), 5)

        if centerX < restraintLeft:
            controls.left()
        elif centerX > restraintRight:
            controls.right()
        else:
            controls.fire()

    cv2.imshow('Video Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()