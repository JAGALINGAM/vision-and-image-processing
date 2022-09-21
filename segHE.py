# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:59:31 2022

@author: Admin
"""


# Let us add some noise to the input image and do the image segmentation
from skimage import io
from matplotlib import pyplot as plt
import numpy as np

img = io.imread("noise.tif")
#plt.imshow(img, cmap=plt.cm.gray, interpolation='nearest')  

#Let's clean the noise using edge preserving filter.
#To denoise, use non-localization means - it works as floating integers (convert the image to float)

from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float

#ubyte -  after processing convert float to  Uint8it (0-255)

float_img = img_as_float(img)
sigma_est = np.mean(estimate_sigma(float_img, multichannel=True))


denoise_img = denoise_nl_means(float_img, h=15 * sigma_est, fast_mode=False, 
                               patch_size=5, patch_distance=3, multichannel=True)
                           
denoise_img_as_8byte = img_as_ubyte(denoise_img)
#plt.imshow(denoise_img_as_8byte, cmap=plt.cm.gray, interpolation='nearest')

#Let's look at the histogram to see howmany peaks we have. 
#Then pick the regions for our histogram segmentation.

#plt.hist(denoise_img_as_8byte.flat, bins=100, range=(0,200))  #.flat returns the flattened numpy array (1D)
#flat the 2D array to 1D array
#from the histogram, i define the range for each segmentation
#identify the separation of regions using histogram
#seg1 is the binary image, all the pixels are extracted from the denoise ubyte, all pixels are <=25
segm1 = (denoise_img_as_8byte <= 25)
segm2 = (denoise_img_as_8byte > 25) & (denoise_img_as_8byte <= 75)
segm3 = (denoise_img_as_8byte > 75) & (denoise_img_as_8byte <= 125)
segm4 = (denoise_img_as_8byte > 125)

#How to show all these segmented images in single visualization?
#each segment in different color
#Construct a new empty image with same shape as original except with 3 layers.
#print(denoise_img.shape[0])
all_segments = np.zeros((denoise_img_as_8byte.shape[0], denoise_img_as_8byte.shape[1], 3)) #nothing but denoise img size but blank
#create the blank image that is same as denoise_ubyte image segment



all_segments[segm1] = (1,0,0)
all_segments[segm2] = (0,1,0)
all_segments[segm3] = (0,0,1)
all_segments[segm4] = (1,1,0)
plt.imshow(all_segments)

#Lot of yellow dots, red dots and stray dots. how to clean
#We can use binary opening and closing operations. Open takes care of isolated pixels within the window
#Closing takes care of isolated holes within the defined window

from scipy import ndimage as nd

segm1_opened = nd.binary_opening(segm1, np.ones((3,3)))
segm1_closed = nd.binary_closing(segm1_opened, np.ones((3,3)))

segm2_opened = nd.binary_opening(segm2, np.ones((3,3)))
segm2_closed = nd.binary_closing(segm2_opened, np.ones((3,3)))

segm3_opened = nd.binary_opening(segm3, np.ones((3,3)))
segm3_closed = nd.binary_closing(segm3_opened, np.ones((3,3)))

segm4_opened = nd.binary_opening(segm4, np.ones((3,3)))
segm4_closed = nd.binary_closing(segm4_opened, np.ones((3,3)))

all_segments_cleaned = np.zeros((denoise_img_as_8byte.shape[0], denoise_img_as_8byte.shape[1], 3)) #nothing but 300, 300, 3

all_segments_cleaned[segm1_closed] = (0,0,1)
all_segments_cleaned[segm2_closed] = (0,1,0)
all_segments_cleaned[segm3_closed] = (1,0,0)
all_segments_cleaned[segm4_closed] = (1,1,0)

plt.imshow(all_segments_cleaned)  #All the noise should be cleaned now