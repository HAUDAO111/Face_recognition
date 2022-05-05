import cv2 as cv
import numpy as np
import os

print('Input your name')
name = input()
try:
    os.mkdir('dataset/'+ name)
except:
    print('ten cua ban da trung lap tao ten moi')
    name = input()
    os.mkdir('dataset/' +name)
face_cascade = cv.CascadeClassifier()
face_cascade.load('face_cascade.xml')

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('Can not turn on the camera')
    exit()
i = 0
while True:
    ret,frame = cap.read()
    if not ret:
        print('Can not return frame')
        break
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
        roi = frame[y:y+h,x:x+w]
    cv.imshow('cam',frame)
    if cv.waitKey(1) == ord('q'):
        break
    if cv.waitKey(20) == ord('k'):
        cv.imwrite('dataset/'+ name +'/'+ name +'_'+str(i)+'.jpg',roi)
        i += 1
cap.release()
cv.destroyAllWindows()