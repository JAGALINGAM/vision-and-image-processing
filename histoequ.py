# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:59:00 2022

@author: Admin
"""

#Histogram equilization (HE) is - histogram of pixel intensity is strechted to both extremes are called as histogram equalization


#Through HE, enhance the contrast of an image

#The information in the image contained in a specific range

#by streching the histogram, the contrast is improved. 

#if we have low contrast image, if we strech the histogram of it, then we get the brighter image

#problem in HE is if the input image is noisy (low contrast), when it is enhanced

#bright is turned to too bright and dark is turned to too dark

#To overcome this problem we have CLAHE

#Contrast limited Adaptive histogram equalization

#It divides the image into small bocks (8*8 tiles default in openCV)

#in each block it performs the histogram equalization

#To minimize the noise amplification - contrast limited is adopted, default value is 40
 

import cv2
from matplotlib import pyplot as plt
img =cv2.imread('Colorimage.jpg')

#converting image to LAB color

lab_image=cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

#run the above lines and see in VE

#in VE we can see three channels in the img variable

#Converting image to LAB

#Luminance (gray scale component of image)
#A is one color space
#B is another color space

#RGB is divided into A and B

#L contains all the information of gray part of image


#split the lab_image to L, A, B channels

l, a, b =cv2.split(lab_image)

#histogram of l component

plt.hist(l.flat, bins=100, range=(0,255))
plt.show()

#Apply histogram equalization on L channel

equ = cv2.equalizeHist(l)
plt.hist(equ.flat, bins=100, range=(0,255))
plt.show()


#combine the hist equalized l channel back to A and B channel

updated_lab_img1 = cv2.merge((equ, a, b))

#Convert the LAB image back to color(RGB)

hist_eq_image =cv2.cvtColor(updated_lab_img1, cv2.COLOR_LAB2BGR)


#Apply CLAHE to L channel
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
clahe_img = clahe.apply(l)

#PLot the histogram
plt.hist(clahe_img.flat, bins=100, range=(10, 255))

#combine the CLAHE enhanced L-channel back to A and B
updated_lab_img2 = cv2.merge((clahe_img, a, b))

#Convert the LAB image back to color(RGB)

CLAHE_img = cv2.cvtColor(updated_lab_img2, cv2.COLOR_LAB2RGB)
"""plt.show('original image', img)
plt.show('equalized image', hist_eq_image)
plt.show('CLAHE IMAGE', CLAHE_img)"""


cv2.imshow('original image', img)
cv2.imshow('equalized image', hist_eq_image)
cv2.imshow('CLAHE IMAGE', CLAHE_img)
cv2.waitKey(0)
