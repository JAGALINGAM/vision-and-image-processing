# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:47:57 2022

@author: Admin
"""

#inverselog is applied on the lighter image to make it darker

#apply the inverse transform on single dimension value



"""from matplotlib import pyplot as plt
import numpy as np
from matplotlib.colors import NoNorm
r = np.arange(0, 255)
c=255/(np.log(1+255))
y=np.exp(r)**(1/c)-1
plt.plot(r,y)"""

#Apply Inverse log transform on image

from skimage import io
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.colors import NoNorm
img = io.imread('lighterimage.tif')
c=255/np.log(1+255)
inverse_log_image = np.exp(img**1/c)-1
inverse_log_image = np.array(inverse_log_image, dtype=np.uint8) #float is converted to int8
plt.figure(figsize=(8,4))
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray', norm=NoNorm())
plt.subplot(1, 3, 2)
plt.imshow(inverse_log_image, cmap='gray', norm=NoNorm())
#plt.imshow(log_image, cmap='gray')
plt.show()


