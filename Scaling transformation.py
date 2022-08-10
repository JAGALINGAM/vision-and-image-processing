# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:02:47 2022

@author: Admin
"""

import cv2
from matplotlib import pyplot as plt
img = cv2.imread('noise.png')
#cv2.imshow(img)
plt.imshow(img)
print(img.shape)
scale_percent = 3.5 # scale the image by 50% width and height of the image is changed by 50%
width = int(img.shape[1] * scale_percent) #image.shape is the original width of the image multipled with the scale percent
# image.shape * scale_percent is float (so converted to int and stored in width)
#shape(1) is the original width (if it is 100, scale percent is 0.50, then 100*0.50 = 50)
height = int(img.shape[0] * scale_percent)
dimension=(width, height)
resize=cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
print(resize.shape)   # to see the new demension
#cv2.imshow('reszied image', resize)
plt.imshow(resize)
#cv2.imwrite('resized image',)"""
#cv2.waitKey(0)

#for upscaling the image increase the value of scale_percent (but resolution is less)


#To resize only tge the height  or only the width
""" in the line 14 change width = int(img.shape[1])  remove scale percent
only the height is changed not width
in the line 17 change height = int(img.shape[0)  remove scale percent
only the width is changed not height


 to fix some number for width and height
 
 remove the line 13, 14, and 17 and specify width = 700, height = 800"""
 
 
