# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:31:14 2022

@author: Admin
"""

# Reading the original image and display the image
#read the image in grayscale

# 8 bit image
import numpy as np
import cv2
img = cv2.imread('lena.tif', 0)
cv2.imshow('input image', img)
cv2.waitKey(0)

#convert the pixel value to the binary.

#Iterate over each pixel and change pixel value to binary.

#How - np.binary_repr()

#store the binary value in the list


list = []   #array 
for i in range(img.shape[0]):   #two for loop - traverse the row and column of image
    for j in range(img.shape[1]):
        list.append(np.binary_repr(img[i][j], width=8))
        


#to see the different value in the list
a = np.array(list)
print(len(a))

#print(len[list])
print(list[25000])    #binary represenation of pixel value 
        
# for the function binary_repr (takes two arguments)

#img[i][j] = pixel value in the ith row and jth col

#width represent the number of bits 

#every pixel in the image is converted to the 8-bit  binary equivalent and stored in list


#step 2:

    # Extraction of bit-plane from the binary equivalent of image
    
#list = binary representation of pixel value

#reshape and reconstruct to obtain the bit images - muliply with 2 to power n-1

eight_bit_plane = (np.array([int(i[0]) for i in list], dtype = np.uint8) * 128).reshape(img.shape[0], img.shape[1]) 

#consider only the eigth bit (it is MSB) for 255  - 1111 1111 

#extract the MSB and convert to the image form.

#extracting the MSB(what is the correspoding pixel value )

#from right 2 power 0, 2 power 1 and.........2 power 7

#msb is 1,multiply with 2 power 7

seven_bit_plane = (np.array([int(i[1]) for i in list], dtype = np.uint8) * 64).reshape(img.shape[0], img.shape[1]) 
six_bit_plane = (np.array([int(i[2]) for i in list], dtype = np.uint8) * 32).reshape(img.shape[0], img.shape[1]) 
five_bit_plane = (np.array([int(i[3]) for i in list], dtype = np.uint8) * 16).reshape(img.shape[0], img.shape[1]) 
four_bit_plane = (np.array([int(i[4]) for i in list], dtype = np.uint8) * 8).reshape(img.shape[0], img.shape[1])
three_bit_plane = (np.array([int(i[5]) for i in list], dtype = np.uint8) * 4).reshape(img.shape[0], img.shape[1]) 
two_bit_plane = (np.array([int(i[6]) for i in list], dtype = np.uint8) * 2).reshape(img.shape[0], img.shape[1]) 
one_bit_plane = (np.array([int(i[7]) for i in list], dtype = np.uint8) * 1).reshape(img.shape[0], img.shape[1])  


#when pixel are connverted to binary form and to bit plane (it is 0 and 1), then if we want to visualize the pixel, then mulitply with 128, 64...and so on.


# list is the 1D array (if the size of the image is 500*1024)

#then the size of the list is  (5,12,000)

#reshape(img.shape[0], img.shape[1]) is to convert the list size to M*N


#step 3:

    #visualize each image corresponding to bit plane
    
    # for better visualization, normalization is used
    
cv2.imshow('bit plane 7', cv2.normalize(eight_bit_plane, np.zeros(img.shape),0,255, cv2.NORM_MINMAX))   
cv2.imshow('bit plane 6', cv2.normalize(seven_bit_plane, np.zeros(img.shape),0,255, cv2.NORM_MINMAX))
cv2.imshow('bit plane 5', cv2.normalize(six_bit_plane, np.zeros(img.shape),0,255, cv2.NORM_MINMAX))  
cv2.imshow('bit plane 4', cv2.normalize(five_bit_plane, np.zeros(img.shape),0,255, cv2.NORM_MINMAX)) 
cv2.imshow('bit plane 3', cv2.normalize(four_bit_plane, np.zeros(img.shape),0,255, cv2.NORM_MINMAX))
cv2.imshow('bit plane 2', cv2.normalize(three_bit_plane, np.zeros(img.shape),0,255, cv2.NORM_MINMAX))
cv2.imshow('bit plane 1', cv2.normalize(two_bit_plane, np.zeros(img.shape),0,255, cv2.NORM_MINMAX))
cv2.imshow('bit plane 0', cv2.normalize(one_bit_plane, np.zeros(img.shape),0,255, cv2.NORM_MINMAX))    


#MSB will have more visual information (eight and seven bit plane)


#how the bit plane slicing used in the image compression


#image is converted to bit plane - for analysing the importance of each bit plane.

#MSB has more information, middle bit plane has subtle details and LSB has zero information

#we can reconstruct the image by considering only the topmost bit plane 

# i can consider only the bit plane 7 6 5 to reconstruct the entire image

#we do not need bit plane 1 to 4 


#image reconstruction using n bit plane 

#combine MSB plane

new_img = eight_bit_plane + seven_bit_plane + six_bit_plane

cv2.imshow('Input image', img)
cv2.imshow('bit plane 8,7,6', new_img)


#represented the original image using only 3 bit plane (require  less space - Image compression 