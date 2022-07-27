

""" Viewing 2D images in python during coding (need to see the output before saving it)
After reading 
process the image
before saving need to see the effect of processing"""


#To visualize 2D image instantly to see the effect of processing. 

#To read the image 

from skimage import io
img = io.imread('grey.tif')
io.imshow(img)


#three ways to visualize the image(skimage, pyplot, opencv)
from matplotlib import pyplot as plt  #using pyplot (can control the visual display(size of the image))
plt.imshow(img)
plt.imshow(img, cmap="hot")  # Cmap tell us in what color we need to show the image

#cmap is applied to the grey scale image, convey the message in easy way

img_gray=io.imread('grey.tif', as_gray=True) #if True is not given then the image is of unsigned integer

plt.imshow(img_gray, cmap="hot")
plt.imshow(img_gray, cmap="jet")

plt.imshow(img_gray, cmap="Blues")