import os
from pathlib import Path
import imutils
import face_recognition
import cv2 as cv
import pickle
import numpy as np  


#build a list of all image 
# img_folder = Path('dataset/hau')
# image_paths = list(img_folder.glob('*.jpg'))
filefolders = os.listdir('dataset')
    #initialize the list of know encoding and know names:
knowEncoding = []
knowName = []
for folder in filefolders:
    img_folder = Path('dataset/'+ folder)
    image_paths = list(img_folder.glob('*.jpg'))
    #loop over the image paths:
    for (i,image_path) in enumerate(image_paths):
        image_path = str(image_path)
        print("[INFO] processing image {}/{}".format(i+1,len(image_paths)))
        basename = os.path.basename(image_path)
        name =  os.path.splitext(basename)[0].split('_')[0]
        #load the input image and convert it from BGR(opencv) to dlib(RGB)
        img = cv.imread(image_path)
        rgb_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)  
        #detect the cordinate of bouding box
        #encoding for each image
        boxes = face_recognition.face_locations(rgb_img,model="hog")
        encodings = face_recognition.face_encodings(rgb_img,boxes)
        for encoding in encodings:
            knowEncoding.append(encoding)
            knowName.append(name)
print("[INFO] serializing encodings...")
data = {"encodings": knowEncoding,"name": knowName}
print(data)
f = open("encodings.pickle","wb")
f.write(pickle.dumps(data))
f.close



    
    
    
