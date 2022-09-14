# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:56:30 2022

@author: Admin
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure, color, io

img1 = cv2.imread("watershed.jpg")
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)




#Threshold image to binary using OTSU. ALl thresholded pixels will be set to 255
ret1, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Threshold', thresh)
cv2.waitKey(0)


print(ret1)

# Morphological operations to remove small noise - opening
#To remove holes we can use closing
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)

cv2.imshow('opening', opening)
cv2.waitKey(0)




from skimage.segmentation import clear_border
opening = clear_border(opening) #Remove edge touching objects
 
cv2.imshow('opening', opening)
cv2.waitKey(0)


#The region far away is background.
#We need to extract sure regions. For that we can use erode. 
#But we have pixels touching each other, so erode alone will not work. 
#To separate touching objects, the best approach would be distance transform and then thresholding.

# let us start by identifying sure background area
# dilating pixes a few times increases object boundary to background. 
# This way whatever is remaining for sure will be background. 
#The area in between sure background and foreground is our ambiguous area. 
#Watershed should find this area for us. 
sure_bg = cv2.dilate(opening,kernel,iterations=2)  #ignore the pixels whixh touches the boundary


cv2.imshow('sure_bg', sure_bg)
cv2.waitKey(0)

# Finding sure foreground area using distance transform and thresholding
#intensities of the points inside the foreground regions are changed to 
#distance their respective distances from the closest 0 value (boundary).

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,3) # map the distance from the pixel to the nearest boundary

cv2.imshow('dist_transform', dist_transform)
cv2.waitKey(0)

#center of the object has max pixel and border of the pixel is lesser intensity
#Using distance transform i cannot complete finding the distance (it is same as opening)
#provide the threshold limit on distance transform (stay close to the center of pixel ) 
#Let us threshold the dist transform by 20% its max value.
print(dist_transform.max()) #gives about 38.200073
ret2, sure_fg = cv2.threshold(dist_transform,0.001*dist_transform.max(),255,0)

cv2.imshow('sure_fg', sure_fg)
cv2.waitKey(0)




#0.2* max value seems to separate the edge.
#High value like 0.5 will not recognize some boundaries.

# Unknown ambiguous region is nothing but bkground - foreground
sure_fg = np.uint8(sure_fg)

unknown = cv2.subtract(sure_bg,sure_fg)


cv2.imshow('unknow', unknown)
cv2.waitKey(0)


#Now we create a marker and label the regions inside. 
# For sure regions, both foreground and background will be labeled with positive numbers.
# Unknown regions will be labeled 0. 
#For markers let us use ConnectedComponents. 
ret3, markers = cv2.connectedComponents(sure_fg)





#One problem rightnow is that the entire background pixels is given value 0.
#This means watershed considers this region as unknown.
#So let us add 10 to all labels so that sure background is not 0, but 10
markers = markers+10

# Now, mark the region of unknown with zero
markers[unknown==255] = 0   #if my unknow is 255 then my marker is 0
plt.imshow(markers, cmap='jet')   #Look at the 3 distinct regions.

#Now we are ready for watershed filling. 
markers = cv2.watershed(img1,markers)
#The boundary region will be marked -1
#cv2.imshow('markers', markers)
#cv2.waitKey(0)


#Let us color boundaries in yellow. OpenCv assigns boundaries to -1 after watershed.
img1[markers == -1] = [255,0,255]  

img2 = color.label2rgb(markers, bg_label=0)

cv2.imshow('Overlay on original image', img1)
cv2.imshow('Colored', img2)
cv2.waitKey(0)
