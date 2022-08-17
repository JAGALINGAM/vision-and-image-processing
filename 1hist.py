# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:29:59 2022

@author: Admin
"""

# Hist - plot shows Intensity distribution of an image

 
"""import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = np.zeros((100, 100), np.uint8)"""
#creating  image 100 by 100, all the pixels in the image are black



"""cv.imshow('img', img)
cv.waitKey(0)

#How to find the histogram of the image -  several methods:
    
#matplotlib
plt.hist(img.ravel(), 256, [0, 256])

#256 - max number of pixel
#0-255 - range of the pixel
plt.show()""" 

#all the intensity in the image is 0, 100*100 = 10000 (number of pixels)

#x-axis - intensity in the image

#y-axis - total number of pixel

#all pixels in the image is black

#hist - tells the intensity distribution of an image.





# 2) How to add white pixel to the image
"""import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = np.zeros((200, 200), np.uint8)
cv.rectangle(img, (0,100), (200,200), (255), -1)

#(0,100), (200,200) are the demension of image
# 255 pixel value for the created rectangle
#-1 thickness to fill the rectangle

#cv.imshow("img", img)

plt.hist(img.ravel(), 256, [0,256])
plt.show()"""
 
#Half of the image as a black pixel, and half of the image as white pixel

#20000 pixels are black, 2000 pixel are white.


# let us add some more pixels to the image

"""import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = np.zeros((200, 200), np.uint8)
cv.rectangle(img, (0,100), (200,200), (255), -1)
cv.rectangle(img, (0,50), (100,100), (127), -1)

#15000 pixels are black, 20000 pixels are white and 5000 pixels are gray

plt.hist(img.ravel(), 256, [0,256])
plt.show()"""


#let us try to use image for hist
"""import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('grey.tif', 1)
plt.hist(img.ravel(), 256, [0,256])
#plt.imshow(img)
plt.show()"""

#How to find the pixel intensity of different colors. 
"""import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Colorimage.jpg', 1)
b,g,r=cv.split(img)
cv.imshow("img", img)
cv.imshow("img", b)
cv.imshow("img", g)
cv.imshow("img", r)
plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.show()"""


#Histogram plot using cv2\
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 
img = cv.imread('grey.tif')
hist = cv.calcHist([img], [0], None, [10], [0,256])
plt.plot(hist)
    
    