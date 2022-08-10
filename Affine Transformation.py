# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:20:27 2022

@author: Admin
"""
import cv2
import numpy as np 
from matplotlib import pyplot as plt
img =cv2.imread('Colorimage.jpg')
rows, columns, ch = img.shape  #function shape returns the shape of the i/p image
pt1 = np.float32([[50,50], [200,50], [50, 200]])
#pt(point) is defined in the original image, this point should not be co-linear
pt2 = np.float32([[10,100], [200,50], [100, 250]])
matrix = cv2.getAffineTransform(pt1, pt2) #Transform function to create a matrix
new_img = cv2.warpAffine(img, matrix, (columns, rows))
plt.subplot(121), plt.imshow(img), plt.title('input')
plt.subplot(122), plt.imshow(new_img), plt.title('output')


