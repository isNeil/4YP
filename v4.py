# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:11:03 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colour import Color
from scipy.signal import savgol_filter
from spherical import asSpherical
from spherical import asCartesian

import joint_angle as ja


plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3.json')
plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5.json')

#    #index mapping
bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
    
index=15
 
frames=np.shape(plot1)[1]
#joint 0 to 27 Rwrist

angle=[]
angle2=[]




#shoulderstart=np.subtract(start[joints[-2]],start[joints[-3]])
#s_s=asSpherical(shoulderstart)
#shoulderend=np.subtract(end[joints[-2]],end[joints[-3]])
#s_send=asSpherical(shoulderend)
#def res(y):
#    for x in range(len(y)):
#        if y[x]<0:
#            y[x]=360+y[x]             
#    return y
#
#s_s=res(s_s)
#s_send=res(s_send)
#s_diff=np.subtract(s_send,s_s)
#start_temp3=start[joints[-3]]






#mapping index to joint 
dex=joints[index]


for i in range(frames):
    
    angle.append(ja.joint_angle(i,plot1,bones,joints)[index]) #ja.joint_angle returns angles for entire skeleton so select joint using index
    angle2.append(ja.joint_angle(i,plot2,bones,joints)[index])
    
    
########################################Below this should be a function but for now just do x
#dist = savgol_filter(dist, 21, 3) # window size 51, polynomial order 3
#dist2 = savgol_filter(dist2, 21, 3)  
#
#speed=[]
#speed2=[]
#
#
#for i in range(np.shape(plot1)[1]-1):
#    
#    speed.append(dist[i+1]-dist[i])
#    speed2.append(dist2[i+1]-dist2[i])
#
#
#speed = savgol_filter(speed, 21, 3) # window size 51, polynomial order 3
#speed2 = savgol_filter(speed2, 21, 3)  
#
#accel=[]
#accel2=[]
#
#for i in range(np.shape(plot1)[1]-2):
#    
#    accel.append(speed[i+1]-speed[i])
#    accel2.append(speed2[i+1]-speed2[i])


fig = plt.figure(figsize=(10, 5))
#fig, ax = plt.subplots()
plt.plot(angle)
plt.plot(angle2,"r")
plt.ylabel('Angle')
plt.xlabel('Frame')
plt.grid(True)
#ax.set_axisbelow(True)
#ax.minorticks_on()
#ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlim((0,102))
plt.show()



plt.tight_layout()
 

plt.show()