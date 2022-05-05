import cv2 as cv
import pickle
import face_recognition
#import sendimage

print("[INFO] loading encodings...")
data = pickle.loads(open("encodings.pickle","rb").read())

print("[INFO] launching the camera...")
cap = cv.VideoCapture("rtsp://admin:admin@192.168.1.61:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")
if not cap.isOpened():
    print("Can not access to camera")
    exit()
while True:
    ret,frame = cap.read()
    if not ret:
        print("Can not return the frame")
        break

    #convert input frame to rgb image
    rgb_img = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    #resize image:
    rgb_img = cv.resize(rgb_img,(0,0),fx=0.25,fy=0.25)
    #face location and encoding for image input
    boxes = face_recognition.face_locations(rgb_img)
    encodings = face_recognition.face_encodings(rgb_img,boxes)
    face_name = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"],encoding)
        name = "Unknown"
        if True in matches:
            matchedIndex = [i for (i,b) in enumerate(matches) if b]
            count = {} 
            for i in matchedIndex:
                name = data["name"][i]
                count[name] = count.get(name,0)+1
            name = max(count,key=count.get)
        face_name.append(name)
    for (top,right,bottom,left),name in zip(boxes,face_name):
        #scale back up face location 
        top *= 4
        right *= 4
        bottom *=4
        left *=4
        #draw a box around face
        cv.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        #draw label with name below the face:
        cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
        font = cv.FONT_HERSHEY_DUPLEX
        cv.putText(frame,name,(left+6,bottom-10),font,1.0,(255,255,255),1)
        if name ==  "Unknow":
            cv.imwrite('/data',frame)
    cv.imshow('camera',frame)
    if cv.waitKey(1) & 0xFF == ord ('q'):
        break
cap.release()
cv.destroyAllWindows()
