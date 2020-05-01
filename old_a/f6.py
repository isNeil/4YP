# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:11:03 2020

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

#    [0]  = 'Hip'   [1]  = 'RHip'   [2]  = 'RKnee'   [3]  = 'RFoot'   [6]  = 'LHip'   [7]  = 'LKnee'   [8]  = 'LFoot'   [12] = 'Spine'   [13] = 'Thorax'
#    [14] = 'Neck/Nose'   [15] = 'Head'   [17] = 'LShoulder'   [18] = 'LElbow'   [19] = 'LWrist'   [25] = 'RShoulder'   [26] = 'RElbow'   [27] = 'RWrist'

# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm


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
    plot1x.append(plot1.iloc[27][i][0]-plot1.iloc[19][i][0])
    plot1y.append(plot1.iloc[27][i][1]-plot1.iloc[19][i][1])
    plot1z.append(plot1.iloc[27][i][2]-plot1.iloc[19][i][2])
    










#######################################Below this should be a function but for now just do x

fig = plt.figure(figsize=(10, 5))
#fig, ax = plt.subplots()
plt.plot(plot1x)
plt.ylabel('Displacement x')
plt.xlabel('Frame')
plt.grid(True)
#ax.set_axisbelow(True)
#ax.minorticks_on()
#ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlim((0,102))
plt.show()


fig2 = plt.figure(figsize=(10, 5))
plt.plot(plot1y)
plt.ylabel('Displacement y')
plt.xlabel('Frame')
plt.grid(True)
plt.xlim((0,102))
plt.show()


fig3 = plt.figure(figsize=(10, 5))
plt.plot(plot1z)
plt.ylabel('Displacement z')
plt.xlabel('Frame')
plt.grid(True)
plt.xlim((0,102))
plt.show()


plt.tight_layout()
 

plt.show()