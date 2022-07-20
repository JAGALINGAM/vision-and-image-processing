# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:06:22 2022

@author: Admin
"""

"""from PIL import Image  #it does not import image as a numpy array
image=Image.open('noise.png')
print('Image size=', image.size, 'image format=', image.format)"""

"""import skimage
from skimage import io
img3=io.imread('noise.png')
print(img3.shape)"""

#convert the image to floating point

"""from skimage import img_as_float
img4 = img_as_float(img3)"""

#import multiple module at the same time
#from skimage import  io, img_as_float

#if we convert the int to float using numpy
#the values are in the float  but it did not scaled b/w 0 to 255.

#import numpy as np
#img5 = img3.astype(np.float)


#read the image using opencv
#size and dimension of the image remain same but the value are different
#opencv read image in BGR instead of RGB

"""import cv2
img5 = cv2.imread('noise.png')"""

#To open grey image
#import cv2
#grey_img = cv2.imread('grey.tif',0)


#import cv2
#grey_img = cv2.imread('grey.tif', 1)  #for color image 1, by defualt it is color image

#cv2 reads the image in BGR

"""import skimage
from skimage import io
img3=io.imread('noise.png')
print(img3.shape)"""


import cv2
img5 = cv2.imread('noise.png', 1)     # to convert to RGB
img7= cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)


