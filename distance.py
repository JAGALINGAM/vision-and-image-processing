# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:29:05 2022

@author: jai
"""

"""Toplogical operation - deals with the spatial arrangment of pixels

arrangement of pixel - constitute an image

Helps to understand the relationship b/w pixels
   1) find the nearest pixel with the same intensity
   2) to find the distance b/w any two pixels in an image.

create a image with black backround(pixels are 0), in the image create two pixel red (P) and green (q)

create the image size 36*36 manually. choose the red and green pixel in 36*36.

Implement euclidean distance method to find the distance"""


import numpy as np
import cv2
from PIL import Image  #Python image library - manipulating the image
import math
from matplotlib import pyplot as plt

#create a image with red and green pixels at the desired location
image = np.zeros((36,36,3), np.uint8)

#selection of red pixel location
image[10,15] = [255,0,0] # 0 - B, 0 -G, 255 - Red

#Choose green pixel location

image[21,23] = [0, 255, 0]

cv2.imwrite('created_image.jpeg', image)
plt.imshow(image) 

#To find the distance between the pixels
x1, y1, x2, y2 = 10, 15, 21, 23
distance = math.sqrt((x2-x1)**2 -(y2-y1)**2)
print(distance)