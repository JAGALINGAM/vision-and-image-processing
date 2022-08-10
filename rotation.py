# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:43:27 2022

@author: Admin
"""

import cv2
from matplotlib import pyplot as plt
img=cv2.imread('grey.tif', 0)
plt.imshow(img)
rows, cols = img.shape  
#grey image as two parameter (rows and columns, not the channel)
# demension of rows and cols of the image are obtained by the shape function
matrix = cv2.getRotationMatrix2D((rows/2, cols/2), 60, 1)
#matrix =cv2.getRotationMatrix2D((rows/2, cols/2), 60, 2.5)
#to rotate the image from the centre of the image rows/2, colum/2
#60 degree to rotate, 1 it preserves the size of the original image
new_img = cv2.warpAffine(img, matrix, (500, 320))
new_img = cv2.warpAffine(img, matrix, (rows, cols))
#img = each pixel in the original image is multipled with the matrix
#after multiplication new pixel location are stored in the new_img     

#cv2.imshow('output', new_img)
plt.imshow(new_img)


# for color image
#rows, cols, ht = img.shape

#How to scale down
#matrix =cv2.getRotationMatrix2D((rows/2, cols/2), 60, 0.5)

#To zoom in
#matrix =cv2.getRotationMatrix2D((rows/2, cols/2), 60, 2.5)


#To change the resolution 
#new_img = cv2.warpAffine(img, matrix, (500, 320))  the image is cut down
 