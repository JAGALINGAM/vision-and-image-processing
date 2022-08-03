# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:16:38 2022

@author: Admin
"""


""" In scikit library, use modlue named transform.

In the transform module have different function like rescale, resize and so on

When you read a color image (line 19, for gray=True is conversion of color image to gray)

Type of the original image is uint8, when you do conversion the type change to float64 (values are b/w 0 to 1)

Gray_False - will not convert the color image to gray image and type is uint8 and can see three channels

Coversion of float by default in scikit image is range(0,1)"""

from matplotlib import pyplot as plt
from skimage import io
from skimage.transform import rescale, resize, downscale_local_mean
img = io.imread('Colorimage.jpg', as_gray=True)
plt.imshow(img)

#After I read the image Perfom transformation operation

""" For rescale - use rescale module, rescale the image by  1/4 (0.25), rescale for 25% 

Anti_aliasing True - removes jagged edges by adding subtle color changes around the lines"""


""" Resized image - image is rezied by 200, 200"""

#img_rescaled = rescale(img, 1.0/4.0, anti_aliasing=True)
#img_resized = resize(img, (50, 100), anti_aliasing=True)
#plt.imshow(img)
#plt.imshow(img, cmap='gray')
#plt.imshow(img_rescaled, cmap='gray')
#plt.imshow(img_resized, cmap='gray')
img_downscaled = downscale_local_mean(img, (8,3))   # it strech the image by 8 by 3
plt.imshow(img_downscaled, cmap='gray')