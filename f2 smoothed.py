# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:56:39 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from colour import Color
import time
from scipy.signal import savgol_filter
from scipy.signal import convolve
from scipy.signal import medfilt
from scipy.ndimage import gaussian_filter
plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3.json')
#plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5.json')

#VELOCITY plot1 - NOTE NEGATIVE VELOCITY WAS CALCULATED SO NEED TO *-1 line 38
#plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3vel.json')
#plot2vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5vel.json')
#plot1accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3accel.json')
#plot2accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5accel.json')

#    #index mapping
bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
    
index=16
 
frames=np.shape(plot1)[1]
#joint 0 to 27 Rwrist
plot1x=[]
plot1y=[]
plot1z=[]
#mapping index to joint 
dex=joints[index]

for i in range(np.shape(plot1)[1]):
    plot1x.append(plot1.iloc[dex][i][0])
    plot1y.append(plot1.iloc[dex][i][1])
    plot1z.append(plot1.iloc[dex][i][2])
    
    
plot1x = savgol_filter(plot1x, 21, 3) # window size 51, polynomial order 3
plot1y = savgol_filter(plot1y, 21, 3)  
plot1z = savgol_filter(plot1z, 21, 3)

    
plot1x = gaussian_filter(plot1x,1)
plot1y = gaussian_filter(plot1y,1)   
plot1z = gaussian_filter(plot1z,1)

 

   #calculate vel
tempx=[]
tempy=[]
tempz=[]

for i in range(np.shape(plot1)[1]-1):
    
    tempx.append(plot1x[i+1]-plot1x[i])
    tempy.append(plot1y[i+1]-plot1y[i])
    tempz.append(plot1z[i+1]-plot1z[i])
    
plot1x=tempx
plot1y=tempy
plot1z=tempz

#######################################Below this should be a function but for now just do x

fig = plt.figure(figsize=(10, 5))
#fig, ax = plt.subplots()
plt.plot(plot1x)
plt.ylabel('Velocity x')
plt.xlabel('Frame')
plt.grid(True)
#ax.set_axisbelow(True)
#ax.minorticks_on()
#ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlim((0,102))
plt.show()


fig2 = plt.figure(figsize=(10, 5))
plt.plot(plot1y)
plt.ylabel('Velocity y')
plt.xlabel('Frame')
plt.grid(True)
plt.xlim((0,102))
plt.show()


fig3 = plt.figure(figsize=(10, 5))
plt.plot(plot1z)
plt.ylabel('Velocity z')
plt.xlabel('Frame')
plt.grid(True)
plt.xlim((0,102))
plt.show()


plt.tight_layout()
 

plt.show()