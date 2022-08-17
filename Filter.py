# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:05:34 2022

@author: Admin
"""


#Smoothing operation is used to remove the noise in the image

#Different kind of filters are

#linear filter, Homogeneous filter, gaussian filter, median, bilateral


#Kernel is convolution matrix (or) mask, small matrix used for blurring, sharpening and edge detection


#In HF, k=1/Kwidth.Kheight (multiplied with kernel matrix)

#Kwidth  - width of the kernel

#Kheight - height of the kernel

#Kernel size is 5 * 5, width is 5 and height is 5.

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('salt_pepper.png')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting image from BGR to RGB

#opencv read the image in BGR format

#define the kernel with 5 by 5
kernel=np.ones((5,5), np.float32)/25

out_img=cv2.filter2D(img, -1, kernel)
blur=cv2.blur(img, (5,5))

gblur=cv2.GaussianBlur(img, (5,5), 0)

median =cv2.medianBlur(img, 5)

bilateralfilter = cv2.bilateralFilter(img, 9, 75, 75)
#img - input image
#-1 desired depth of output image
#Apply kernel on the image using filter 2D
"""titles = ['image', '2Dconvolution']
images=[img, out_img]""" 


titles = ['image', '2Dconvolution', 'blur', 'gblur', 'median', 'bilateralfilter']
images=[img, out_img, blur, gblur, median, bilateralfilter] 

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
    
#output image is smoothed (or blured bit)


#LPF -  helps to remove the noise
#HPF -  To find the edges in the image


#To have blur image 

#blur=cv2.blur(img, (5,5))

#result of 2D and blur is close, because the size of kernel is same



#Gaussian filter - using different weight kernel in both x and y direction.

#Therefore the pixel located in the middle of the kernel has a bigger weight.

#The weight decreaseas with distance from neighbhourhood center pixel.

#In the side we have less weight pixel, in the center it is high

#gblur=cv2.GaussianBlur(img, (5,5), 0)

#0 is sigma

#output from the gaussian filter is much more better.


#GF - designed to remove the high frequency noise

#median filter - replace the each pixel value with the median of it neighbhour pixels

#this filter is good when we have slat and pepper noise.

#in SP image pixels are distored

#in the black pixels we have white pixel noise

#in the white pixel we have black pixel noise

#white pixels are distored like salt, and black pixels were distored like pepper.

# median = cv2.medianBlur(img, 5)


#Bilateral filter -  by using HF median, GF - it dissolve the noise and also smooth the edges.

#but if you want to preserve the edge, to sharpen the edge use bilateral filter

#bilateralfilter = cv2.bilateralfilter(img, 9, 75, 75)

#9 -  diameter of each pixel 

# 75, sigma color -  filter sigma in the color space.

#sigma space - filter sigma in the co-ordinate space.

# edges are preserved in better way.

#hat broder is preserved.

#it removes the noise and also keep the edges sharp.





 
