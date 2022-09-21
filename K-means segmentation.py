# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:11:55 2022

@author: Admin
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("seg3.tif")



#in the VE,  M=448 N=425, 3 - channel (convert MxNx3 to k = MxN)
img2 = img.reshape((-1,3))  #-1 reshape means, in this case MxN


# covert the datatype of img2 to float datatype (it is required of the k-means method of OpenCV)
img2 = np.float32(img2)

#Define criteria, number of clusters and apply k-means
#When this criterion is satisfied, the algorithm iteration stops. 
#cv.TERM_CRITERIA_EPS — stop the algorithm iteration if specified accuracy, epsilon, is reached.
#cv.TERM_CRITERIA_MAX_ITER — stop the algorithm after the specified number of iterations, max_iter.
#cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER — stop the iteration when any of the above condition is met.
#Max iterations, in this example 5. 
#Epsilon, required accuracy, in this example 1.0

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Number of clusters
k = 3

# Number of attempts, number of times algorithm is executed using different initial labelings.
#Algorithm return labels that yield best compactness.

#K-Means provides three output
#compactness : It is the sum of squared distance from each point to their corresponding centers
#2)label.
#3)center of each clusters

attempts = 3

#other flags needed as inputs for K-means
#Specify how initial seeds are taken.
#Two options, cv.KMEANS_PP_CENTERS and cv.KMEANS_RANDOM_CENTERS

#To take the initial center cv.KMEANS_PP_CENTERS

ret,label,center=cv2.kmeans(img2, k, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)

#cv2.kmeans outputs 2 parameters.
#1 COmpactness. 
#2 Labels: Label array.
#3 Center. the array of centers of clusters. For k=4 we will have 4 centers.
#For RGB image, we will have center for each image, so total 4x3 = 12.
#Now convert center values from float32 back into uint8.
center = np.uint8(center) 

#Next, we have to access the labels to regenerate the clustered image
res = center[label.flatten()]    #shape of the label is 190400 (448x425 - original shape of the image)
res2 = res.reshape((img.shape)) #Reshape labels to the size of original image
cv2.imwrite("segmented.jpg", res2)



#Now let us visualize the output result



titles = ['original image', 'segmentation image']
images = [img, res2]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
