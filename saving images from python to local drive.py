# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:11:32 2022

@author: Admin
"""

#read the image
from skimage import io
img = io.imread('grey.tif')

#do processsing on the image read

from skimage import filters
gaussian_img = filters.gaussian(img, sigma=3)

#after applyig filter th type of the image is float and size remains same.
#for float64 - the values are between 0 to 1.
#for unsigned integer8 - the values are between 0 to 255.

#how to save the image
io.imsave('grey1.jpeg', gaussian_img) # saved image is blured, because the skimage 
#converts the floating image to unsignedint8

#To avoid the blurness

from skimage import img_as_ubyte  #convert any other format to 8bit format
gaussian_img_8bit=img_as_ubyte(gaussian_img)

#to save the processed image
io.imsave('grey2.jpeg', gaussian_img_8bit)

#using opencv

# to save the image use imwrite function
import cv2
cv2.imwrite('grey3.jpeg', gaussian_img)

#open the grey3.jpeg image, we see all dark pixels, because opencv converts
#the floating image to all 0 pixels, therefore we see all dark, it does not scale  0 to 255

import cv2
cv2.imwrite('grey4.jpeg', gaussian_img_8bit)

#"""how to provide a solution, opencv handle image as BGR, need to covert from BGR to RGB

import cv2
gaussian_img_8bit_RGB = cv2.cvtColor(gaussian_img_8bit, cv2.COLOR_BGR2RGB)

#cvtColor function is available in cv2 to convert gaussian_img_8bit from BGR to RGB


#save using matplotlib

from matplotlib import pyplot as plt
plt.imsave('grey5.jpeg', gaussian_img)

#for TIFF FILE
import tiffile
tiffile.imwrite('grey.tif', gaussian_img_8bit)


