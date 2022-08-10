# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:27:58 2022

@author: Admin
"""

# IMport libraries 

import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
#from PIL import Image

#To read the original image
img = cv2.imread('grey.tif')

#Max intesity based quantization
L=img.max()

#subtract each intensity from max to obtain the negative
negative = L-img
plt.subplot(221), plt.imshow(img), plt.title('input image')
plt.subplot(222), plt.imshow(negative), plt.title('negative image')


# Find the maximum intensity value and subtract each intensity from the maximum to get the negative value.