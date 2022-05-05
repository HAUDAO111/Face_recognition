.")
cap = cv.VideoCapture(0)
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