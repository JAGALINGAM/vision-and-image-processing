# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:51:06 2022

@author: Admin
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Colorimage.jpg')
plt.imshow(img)
#cv2.imshow('input image', img)

#extent the height and width of the  image

height, width = img.shape[:2]
print(height, width)

#Translate the height and width of the image to 1/4

height_fourth, width_fourth = height/4, width/4

print(height_fourth, width_fourth)

#Translate matrix

t = np.float32([[1,0,height_fourth], [0,1, width_fourth]])
#data type is float 32, element of translation matrix is shown as [1,0,tx] [0,1,ty]

# height of the image/4, width of the image/4
#line27, input image is translated to T

#print the value of translation matrix

print(t)

#using warpaffine translate the image using translation matrix

translation=cv2.warpAffine(img, t, (width, height))
plt.imshow(translation)

#showing the image o/p

#cv2.imshow('Translation', translation)
 
 
