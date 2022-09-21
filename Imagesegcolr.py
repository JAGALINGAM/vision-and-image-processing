# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:07:59 2022

@author: Admin
"""

from skimage import io, measure
import cv2
from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage as nd
from skimage import img_as_ubyte, img_as_float

img = io.imread('D:/VIT/Fall 22-23/Vision and Image Processing/lab/colorseg.jpg')
plt.imshow(img)


#In the input image, we have bunch of colors, we segment image on pixel based on the specific color

#convert the RGB to different color space (HSV)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
#hsv demension is same as input image

mask = cv2.inRange(hsv, (100, 90, 90), (120, 255, 255)) 

#mask is created - threshold the image by slecting the blue color.

#at center dark blue, at edge -light blue H is 100 to 120

#sat - 90 to 255 and V is from 90 to 2355

#mask =cv2.inRange(hsv, (0,0,100), (180, 70, 255)) for white color

plt.imshow(mask)

#in the output i have some holes - to close it i use binary closing operation
#(dilation followed by erosion)


closed_mask = nd.binary_closing(mask, np.ones((5,5)))
plt.imshow(closed_mask)



#after segmentation each object given a unique label value
label_image = measure.label(closed_mask)
plt.imshow(label_image)



from skimage.color import label2rgb
image_label_overlay = label2rgb(label_image, image=img)
#it takes the original image and overlay the label image on top of that in RGB

#in the input image the blue balls are in different color and all other colors of ball are black and white


plt.imshow(image_label_overlay)
img_as_8byte = img_as_ubyte(image_label_overlay)



#To calculate image properties (area, centroid, convex_area, label, intensity image, major axis length and so on)
#import this data as pandas-compatible table.

props = measure.regionprops_table(img_as_8byte, img, properties=['label', 'area'])

import pandas as pd
df = pd.DataFrame(props)
print(df.head())



