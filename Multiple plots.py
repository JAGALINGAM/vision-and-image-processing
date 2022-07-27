from skimage import io
img = io.imread('grey.tif')
io.imshow(img)


# create the place holder called fig which is of size 10 by 10.

#in the fig create a variable called ax1, ax2, ax3, ax4

# I have a grid 10 by 10, in that i add a subplot.

# (2, 2, 1) i create  2 rows, 2 columns, 1-first position

 # (2, 2, 2) i create  2 rows, 2 columns, 2-second position



from matplotlib import pyplot as plt  
fig = plt.figure(figsize=(10, 10)) 


ax1=fig.add_subplot(2, 2, 1) # create a variable called axis 1, 2, 3, 4
ax1.imshow(img, cmap='hot')
ax1.title.set_text('1st')

ax2=fig.add_subplot(2, 2, 2) # create a variable called axis 1, 2, 3, 4
ax2.imshow(img, cmap='jet')
ax2.title.set_text('2nd')

ax3=fig.add_subplot(2, 2, 3) # create a variable called axis 1, 2, 3, 4
ax3.imshow(img, cmap='gray')
ax3.title.set_text('3rd')

ax4=fig.add_subplot(2, 2, 4) # create a variable called axis 1, 2, 3, 4
ax4.imshow(img, cmap='Blues')
ax4.title.set_text('4th')






