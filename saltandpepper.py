# -*- coding: utf-8 -*-
"""cv2.destoryAllWindows()
Created on Wed Sep 14 12:10:44 2022

@author: Admin
"""
    


import cv2
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt 

img = cv2.imread('lena.tif', 0)
img = img/255

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#create a blank image using numpy zero function

x, y = img.shape
g = np.zeros((x,y), dtype=np.float32)  #size of the blank image should be same as original image

cv2.imshow('image1', g)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Randomly fill the value in the blank image

#salt and pepper value is

pepper = 0.05
salt = 1-pepper

# create the salt and pepper noise image



#for every row and column in the blank image , generate the random number using np.random
#it creates the random number from 0 to 1
#if the random number is <0.05, fill the value in the blank image as 0.
#if the random number is >salt than fill as 1

#if the random value is b/w the pepper and noise then fill the blank image with pixel value = original image
#this for loop repeats all row and column in the balnk image.
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]
            
            
cv2.imwrite("noise.tif", g)
cv2.imshow('image with noise', g)

cv2.waitKey(0)
cv2.destroyAllWindows()
      

