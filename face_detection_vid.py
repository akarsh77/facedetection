import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To use a video file as input 
cap = cv2.VideoCapture('vid.mp4')

while True:
    # Read the frame
    _, img=cap.read()
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.25, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display 
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture  object
cap.release()