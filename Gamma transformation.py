# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:32:26 2022

@author: Admin
"""

#used to map the narrow range of dark input values to wider range of output values.

import cv2
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math

img = cv2.imread('grey.tif', 1) # 0 reads as a grey scale image
gamma = 2   # gamma transform
img_gamma1 = np.power(img, gamma)  #raising the image by gamma(2) 

gamma = 10
img_gamma2 = np.power(img, gamma) 


gamma = 20
img_gamma3 = np.power(img, gamma) 

plt.subplot(221), plt.imshow(img), plt.title('input image')
plt.subplot(222), plt.imshow(img_gamma1), plt.title('gamma=2')
plt.subplot(223), plt.imshow(img_gamma2), plt.title('gamma=10')
plt.subplot(224), plt.imshow(img_gamma3), plt.title('gamma=20')