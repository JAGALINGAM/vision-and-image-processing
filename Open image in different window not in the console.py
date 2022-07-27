# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:17:16 2022

@author: Admin
"""

import cv2
gray_img = cv2.imread("grey.tif", 0)  #0 - to read the image in the grey 
color_img = cv2.imread('grey.tif', 1)  
cv2.imshow("colur image", color_img)
cv2.imshow("gray_img", gray_img)

# the colo_img and gray_img is shown in the different window.

#How long the window need to be available 

#cv2.waitKey(0) # we close the window, when it not needed
cv2.waitKey(3000) # the window will be opened for 3 milliseconds

cv2.destroyAllWindows()