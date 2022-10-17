# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:21:14 2022

@author: Admin
"""

""" What is fourier transform (FT)?

FT -  breaks a function (signal) into an alternate respresenation 

representation using - sine and cosines 


What FT shows?  any signal can be reconstruted by summing up 
individual sine waves of different frequencies """


import cv2
from matplotlib import pyplot as plt
import numpy as np

# For generating the two-demensional sin waves image
x = np.arange(256)  # generate values from 0 to 255 (our image size)
y = np.sin(2 * np.pi * x / 4)  #calculate sine of x values, this defines the frequency 
#Divide by a smaller number above to increase the frequency.
y += max(y) # offset sine wave by the max value to go out of negative range of sine 

#Generate a 256x256 image (2D array of the sine wave)
img = np.array([[y[j]*127 for j in range(256)] for i in range(256)], dtype=np.uint8) # create 2-D array of sine-wave

plt.imshow(img)
#img = np.rot90(img)  #Rotate img by 90 degrees

#run the above line of code - output is certain sin wave of frequency

#in the line 25 - decrease the value of frequency, change the value 3 to 20

# The frequency changes - by changing the value. 

img = cv2.imread('lena.tif', 0) # load an image

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

#in opencv function name is dft

#dft apply on the float value 

#to inculde complex number in the output. 

#Shift DFT. First check the output without the shift
#Without shifting the data would be centered around origin at the top left
#Shifting it moves the origin to the center of the image. 
dft_shift = np.fft.fftshift(dft)

#dft_shift = dft

#low pass in the center and high pass in around the edges. 

#Calculate magnitude spectrum from the DFT (Real part and imaginary part)
#Added 1 as we may see 0 values and log of 0 is indeterminate
magnitude_spectrum = 20 * np.log((cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))+1)

# line 60 - in VE it does not have 2 - it do not have imagery component 

#dft_shift[:, :, 0] - real component all pixels in x and all pixels in y and 0 is real number

#dft_shift[:, :, 1]) - 1 is  imagery component 

# in line 43 - see VE 256, 256, 2 (1- real number, 2- imagnery numbers )

#in line 54, the top left corner pixels in the image shifted to the center 

#remove the DFT shift line 54  and execute the line 56 (we do not shift)

#IN the FFT image not showing anything - because the signal is all around 0.

#now execute the line 54 and see the difference in the output. 

#As the spatial frequency increases, points are closer


#the peaks in the DFT amplitude spectrum move farther away from the origin

#Center represents low frequency and the corners high frequency (with DFT shift).
#To build high pass filter block center corresponding to low frequencies and let
#high frequencies go through. This is nothing but an edge filter. 

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(magnitude_spectrum)
ax2.title.set_text('FFT of image')
plt.show()


#Devloped a sin wave and their fourier transform