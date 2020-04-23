# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:52:55 2020

@author: neilw
"""

from PIL import Image  
  
# Opens a image in RGB mode  
#for i in range(10): 
#    for j in range(1,17):
#    
        
#        im = Image.open(r"C:\Users\neilw\Desktop\RF Vpython\Jump\Images\MEASUREmatrix.jpg"%(i,j))  
#  
#        
#          
#        
#        newsize = (650, 325) 
#        im1 = im.resize(newsize) 
#        # Shows the image in image viewer  
#        im1.save(r"C:\Users\neilw\Desktop\RF Vpython\Jump\Images\UIresize\matrixmean.jpg"%(i,j))    
#       
im = Image.open(r"C:\Users\neilw\Desktop\RF Vpython\Jump\Images\UIresize\matrixvarp.png")  
  

newsize = (650, 200) 
im1 = im.resize(newsize) 
# Shows the image in image viewer  
im1.save(r"C:\Users\neilw\Desktop\RF Vpython\Jump\Images\UIresize\matrixvarUSE.png")    
#       