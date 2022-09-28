# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 14:29:30 2022

@author: Admin
"""

import cv2
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt 
img=cv2.imread('lena.tif', 0)
img= img/255
cv2.imshow('orignal image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#create the gaussian noise
x, y =img.shape
#x, y are row and column of the original image
mean =0
var=0.05  # calculate the SD(or)sigma taking SQRT of variance
sigma = np.sqrt(var)
n=np.random.normal(loc=mean, scale=sigma, size=(x,y))
cv2.imshow('gaussian noise', n)
cv2.waitKey(0)
cv2.destroyAllWindows()

#display the probability density function
kde = gaussian_kde(n.reshape(int(x*y)))  #calculate the frequency of random number from gaussian image
dist_space=np.linspace(np.min(n), np.max(n), 100)  #to specify the minmum no of noise and max of noise
plt.plot(dist_space, kde(dist_space))  #to plot the histogram
plt.xlabel('noise pixel value')
plt.ylabel('Frequency')
plt.show()

#to add gaussian noise
g=img+n
cv2.imshow('corrupted image', g)
cv2.waitKey(0)
cv2.destroyAllWindows()

#To display all the image
cv2.imshow('orignal image', img)
cv2.imshow('gaussian noise', n)
cv2.imshow('corrupted image', g)
#cv2.imsave(g)



