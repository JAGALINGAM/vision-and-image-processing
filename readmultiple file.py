# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 19:59:34 2022

@author: Admin
"""

import os
path='D:\VIT\Fall 22-23\Vision and Image Processing\lab'
print(os.listdir(path))

for image in os.listdir(path):
    print(image)
    
""" Os.listdir - returns the list containing the name in the given path"""

"""other way is OS.walk - returns the generator, creates a tuple of value
(current_path, directories in the current _path, files in the current path)"""

"""import os
print(os.walk(".")) #not given any path here (it walk from the current directory path)
#os.walk generate the genartor object in th console window. 
#using generator we can perform some operation

for root, dirs, files in os.walk("\Vision and Image Processing\lab"): 
    print(root)
 #extracting the root directory name, current directory and files
    path =root.split(os.sep)
    print(path)
    print(files)"""