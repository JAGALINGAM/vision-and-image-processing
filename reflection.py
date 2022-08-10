# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:15:08 2022

@author: Admin
"""

import cv2
import matplotlib.pyplot as plt
img = cv2.imread('grey.tif')
plt.subplot(121), plt.imshow(img), plt.title('input')
#img_flip=cv2.flip(img, 0) # img, 0 it flips the image in the horizontal axis
#img_flip=cv2.flip(img, 1) # img, 1 it flips the image in the Vertical axis

img_vh=cv2.flip(img, -1) #To flip at both vertical and horizontal axis

plt.subplot(122), plt.imshow(img_vh), plt.title('fliped image')