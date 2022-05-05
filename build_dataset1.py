import cv2 as cv
import os
from cv2 import rectangle
import face_recognition

print("input your name")
name = input()
try:
    os.mkdir('dataset/'+name)
except:
    print("Ten da trung tao ten moi")
    name = input()
    os.mkdir('dataset/'+name)
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('can not open camera')
    exit()
i = 0
while True:
    ret,frame = cap.read()
    if not ret:
        print("can not return frame")
        break
    img_resize = cv.resize(frame,(0,0),fx=0.25,fy=0.25)
    boxes = face_recognition.face_locations(img_resize,model="hog")
    for top,right,bot,left in boxes:
        top *= 4
        right *= 4
        bot *=4
        left *=4
        #draw a box around face
        cv.rectangle(frame,(left,top),(right,bot),(0,0,255),2)
        roi = frame[top:bot,left:right]
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break
    if cv.waitKey(20) == ord('k'):
        cv.imwrite('dataset/'+ name +'/'+ name +'_'+str(i)+'.jpg',roi)
        i +=1
cap.release()
cv.destroyAllWindows()
