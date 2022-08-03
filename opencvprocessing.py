# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:28:38 2022

@author: Admin
"""

"""import cv2
from matplotlib import pyplot as plt
img=cv2.imread('rgb_image.jpg',1)  #1 read the image in color form, In VE, you have number of channels)
plt.imshow(img) # images were shown in the BGR form. all the red color in the original image is changed to Blue color

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#resize the image using resize function, factor of resize is 2 by 2, output is going to be four time bigger.
#Strech the 


cv2.imshow('orginal img', img)
cv2.imshow('resized img', resized)
cv2.waitKey(0)"""

""" To extract the value at single pixel by pointing at specified pixel"""

"""import cv2
from matplotlib import pyplot as plt
grey_img = cv2.imread('rgb_image.jpg', 0)
color_img=cv2.imread('rgb_image.jpg', 1)
#plt.imshow(grey_img)
#plt.imshow(color_img)
print(grey_img.shape)
print(color_img.shape)
print("Top left", grey_img[0,0])
print("Top left", color_img[0,0])
print("Top right", grey_img[0,400])
print("Bottom right", grey_img[580,200])
print("Bottom right", color_img[580,200])"""


""" Splitting a image by BGR"""

"""import cv2
from matplotlib import pyplot as plt
grey_img = cv2.imread('rgb_image.jpg', 0)
color_img=cv2.imread('rgb_image.jpg', 1)
print(color_img.shape)  # shape of the image is (615, 757, 3)  3 (BGR channels)
blue = color_img[: , : ,0] 
#color_img variable size is 615, 757, 3), 3 is B G R three channels
#[:, :, 0], : is 615, : 757, 0 for Blue

#I want all 615, 757 from the first channel
cv2.imshow('Blue pic', blue)  # all the other color in the image is black and blue color showed in white
red = color_img[: , : ,1]
green = color_img[: , : ,2]  
cv2.waitKey(0)
cv2.destoryAllWindows()"""


"""In VE, the blue green and red size is (615, 757) but no third variable for gray scale image """


#To split the channels in the image we have a function called split
import cv2
#grey_img = cv2.imread('rgb_image.jpg', 0)
color_img=cv2.imread('rgb_image.jpg', 1)
b,g,r = cv2.split(color_img)
cv2.imshow('green pic', b) #blue channel in the original is splited (if you want to process with blue band split, and then merge all the channel)

cv2.waitKey(0)

#How to merge BGR channel

img_merged=cv2.merge((b,g,r))
cv2.imshow("Mergeimage", img_merged)


