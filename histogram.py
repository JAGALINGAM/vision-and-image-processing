# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 11:11:20 2022

@author: Admin
"""

""" What is histogarm - Provides overall idea of the intensity distribution of an image.

It is plot with pixel value  x axis (0-255), y axis(corresponding number of pixels)

Histogram is way to understand the image and provides intuition on contrast brightness of an image

Can plot histogram using openCV and numpy

Terminologies of hist: Bins - image has gray level from 0 to 255

you no need to find number of pixels for all pixels separately.

But number of pixels in a interval of pixel values for e.g need to find number of pixels lying b/w 0 to 14, 16-31....., 240 to 255

need only 16 values to represent the histogarm

DIMS - Number of parameters for which we collect data. For image we collect data only from the intensity, DIMS is one   


Range -  range of the intensity value to measure"""

#Histogram claculation using openCV

#use the function cv.calcHist() function to find the Hist


#cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

#image -  input image
#channel - represent in [], index of a channel for which we cal hist, for gray image - [0], for color_image[0][1][2] to cal hist for B, G, R
#mask - to find the hist of full image, then mask is NONE, to find the hist of particular region in the image use mask
#histSize - represents the bin count []
#ranges - 0 to 255


#Hist for gray image
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('contrast.jpg')
hist = cv2.calcHist([img],[0],None,[10],[0,256])
plt.imshow(hist)

#hist is a 256x1 array, each value corresponds to number of pixels in that image with its corresponding pixel value.

"""import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Colorimage.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()"""


# to find the histogram of full image the function is cv.calcHist() 

#But i want to find the histogram of some region of the image

#create a mask image with white color on the region you want to find histogram and black other regio. 

"""import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('contrast.jpg')


# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:400, 100:300] = 255


masked_img = cv.bitwise_and(img,img,mask = mask)  #first input array, second input array, 
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()"""