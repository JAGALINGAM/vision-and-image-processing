# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:33:06 2022

@author: Admin
"""

"""In the process of image processing, to understand data/information of image, 
plot the data extracted from the image"""


#In plot - we have x and y axis

"""from matplotlib import pyplot as plt
x=[10, 20, 30, 40, 50]       #List
y=[100, 200, 300, 400, 500]
plt.plot(x,y)"""


#plotting using numpyarray

"""from matplotlib import pyplot as plt
import numpy as np
x=[10, 20, 30, 40, 50]       #List
y=[100, 200, 300, 400, 500]
a=np.array(x)    # x is converted to numpy array
b=np.array(y)    # y is converted to numpy array
plt.plot(a,b)"""

#How to plot the image
"""import cv2
from matplotlib import pyplot as plt
gray_img = cv2.imread("grey.tif", 0)  #0 - to read the image in the grey 

#execute first three lines - gray_img is of type uint8
#plt.imshow(gray_img, cmap="gray") # show the image 

#how to show the histogram of the image

#Histogram - How many pixels are bright and dark 

#In VE gray_img is of 2D, for histogram we need 1D, .flat(for 1D)
plt.hist(gray_img.flat, bins=50, range=(0, 100))"""




#more on plotting


"""from matplotlib import pyplot as plt
import numpy as np
a=np.array([10, 20, 30, 40, 50])
b=np.array([100, 200, 300, 400, 500])
#plt.plot(a,b)
#plt.plot(a,b, 'r--') #plot appears red dash line
#plt.plot(a,b, 'g^') #plot appears green triangle dash line
#plt.plot(a, b,'bo')  #plot appers in blue dot
#plt.axis([0,6,0,50]) #Defines the range for (0 to 6 in x and (0 to 50 in y axis)
#plt.plot(a,b, 'r--') #plot appears red dash line"""


#plot using different type of data
"""from matplotlib import pyplot as plt
wells = ['well1','well2', 'well3', 'well4', 'well5']
cells = [80, 62, 88, 100, 90]
plt.bar(wells, cells)
plt.scatter(wells, cells)
plt.plot(wells, cells)"""

#adding labels and annotations
"""from matplotlib import pyplot as plt
wells = ['well1','well2', 'well3', 'well4', 'well5']
cells = [80, 62, 88, 100, 90]
plt.figure(figsize=(5,5))  #figure size is 5 by 5
plt.bar(wells, cells) # bar plot x is wells and y is cells
plt.xlabel('well#', fontsize=20, color='red') #x label is well
plt.ylabel('Dead cells')
plt.title('Dead cells in each wells')
plt.axis([0,6,60,120]) #0-x axis min, 6-x axis max, 60 y axis min, 120 y axis max
plt.grid(True) # place the grid in the plot
plt.show() # to show the graph"""


#logscale plot
"""from matplotlib import pyplot as plt
x=[10, 20, 30, 40, 50]
y=[1, 120, 1300, 1150, 10000]
#x and y for log plotting, fig size is 12, 6
#need to put two plots side by side (one plot is for linear and other plot is for log)
plt.figure(figsize=(12,6))
#linear
plt.subplot(121) 
#to have two plots (1 -row, 2-column, 1-first image)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)
#for log
plt.subplot(122) 
#to have two plots (1 -row, 2-column, 2-second image)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)"""

# In image processing, we try to keep both input and output image side by side
#for better visual interpretation.

#multiple plots using subplot (Horizontally)
"""from matplotlib import pyplot as plt
wells = ['well1','well2', 'well3', 'well4', 'well5']
cells = [80, 62, 88, 100, 90]
plt.bar(wells, cells)
plt.scatter(wells, cells)
plt.plot(wells, cells)"""

#if we plot bar, scatter, plot at a time, chart contains all of this.
#to plot it separately (Horizontally)
"""from matplotlib import pyplot as plt
wells = ['well1','well2', 'well3', 'well4', 'well5']
cells = [80, 62, 88, 100, 90]
plt.figure(figsize=(12,6))
plt.subplot(131)  # 1-row, 3-column, 1-first image
plt.title("bar plot")
plt.bar(wells, cells)
plt.subplot(132)
plt.title("Scatter plot")
plt.scatter(wells, cells)
plt.subplot(133)
plt.title("plot")
plt.plot(wells, cells)
plt.suptitle("Multiple plots")
plt.show()"""

#write the code to display the images in the vertical plot.