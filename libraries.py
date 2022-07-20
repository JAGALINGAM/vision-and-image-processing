# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:26:39 2022

@author: Admin
"""

import skimage   # install scikit-image
from skimage import io   # io (input and output of image)
img = io.imread('noise.png')  #imread is a function from io module


"""import cv2   #install opencv
img1 = cv2.imread('noise.png')""" #imread function is used to read the image

#import numpy as np
#a=np.ones((5, 5))    #5 by 5 matrix is created filled with ones

#import pandas as pd
#df=pd.read_csv('CreditWorthiness.csv')
#print(df.head())


from matplotlib import pyplot as plt
plt.imshow(img)





























