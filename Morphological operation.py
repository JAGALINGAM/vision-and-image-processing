# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 13:43:39 2022

@author: Admin
"""

""" Operation is based on image shape

It perfomred on binary image

To peroform MT - Input image and SE(KERNEL)"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('morpho.tif', cv2.IMREAD_GRAYSCALE)

_, mask =cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# 127 - VALUE OF THRESHOLD

kernel = np.ones((5,5), np.uint8)
#dilation =cv2.dilate(mask, kernel)
dilation =cv2.dilate(mask, kernel, iterations=1)
#In the dilation process black pixel were reduced, or white pixel are incresed.

# To remove the black pixel completely, i apply iteration, apply kernel for any number of iteration.

#bigger the kernel size, black pixel are turned to white, by dilation but size of the white object is increased   

#Dilation -  if atleast one pixel matches with kernel, than change the pixel to 1

#Therefore the shape of white object is increasing. 

erosion = cv2.erode(mask, kernel, iterations=1)

# the shape of the white object is reduced.  erosion - all pixels of image need to be match with kernel, than 1 else 0. 


opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#dilation followed by erosion

#change the kernel size and iteration number and see the difference.

gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
#difference between the dilation and erosion

tophat=cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

#diff b/w the input image and opening image.

titles = ['input image', 'mask', 'dilation', 'erosion', 'opening', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, gradient, tophat]

for i in range(7):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
        
#To apply Morphological operation on the gray scale image, i mask the image by thresholding

#if the input image is binary image, not required need of mask)
