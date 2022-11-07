# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:48:38 2022

@author: Admin
"""


"""In the folder - have some images (dataset), and for comparison of dataset image, i have imported image""" 


import cv2
import face_recognition
from simple_facerec import SimpleFacerec

img=cv2.imread('modi.png')

#rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("Image", img)

#cv2.imshow("Image", rgb_img)

cv2.waitKey(0)


#First step for Face recongnition is to encode the image.

#encode the imported image and comapre with the other images in the folder 


img_encoding = face_recognition.face_encoings(img)[0]


# Repeat the step for another image


img1=cv2.imread('D:/VIT/Fall 22-23/Vision and Image Processing/lab/Frec/images/dhoni.png'  )

#rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("second Image", img1)

#cv2.imshow("Image", rgb_img)


#img1_encoding = face_recognition.face_encoings(img1)[0]

#cv2.waitKey(0)



# Step 3: comparison of images

#comapre the face, if both the images are same it will print true.

result = face_recognition.compare_faces([img_encoding], img1_encoding) 

print("Result:", result)


"""step4: encode all the faces in the dataset  (why - through the webcam video streaming)

if it find a match in the dataset, it shows the name )





#Encode the face from the folder"""

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")  # images/ is the name of the folder contains image


"""Step 4: Face recognition in real-time on a webcam"""

# https://pysource.com/wp-content/uploads/2021/08/source-code-face-recognition.zip

""" From the link above download  simple_facerec.py  (keep this .py file in the image dateset folder)"""


#Step5:   Take webcame stream

cap = cv2.VideoCapture(2)

while True:
    ret, frame=cap.read()
    
    
 
    #Step 5: Face location and face recognition
    
    
#Identify the face passing the frame of the webcam to the function

# detect_known_faces(frame)  - it will give name of the person.


face_locations, face_names = sfr.detect_known_faces(frame)

for face_loc, name in zip(face_locations, face_names):
    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2] 


#step 6: Show name and rectangle

cv2.putText(frame, name, (x1, y1 -10)), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)

cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

cv2.imshow("FRAME", frame)

key = cv2.waitKey(1)

if key == 27;:
    break
