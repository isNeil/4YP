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

plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3.json')
plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5.json')

#    #index mapping
bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
    
index=15
 
frames=np.shape(plot1)[1]
#joint 0 to 27 Rwrist
#plot1x=[]
#plot1y=[]
#plot1z=[]
#
#plot2x=[]
#plot2y=[]
#plot2z=[]

dist=[]
dist2=[]
diff=[]
#mapping index to joint 
dex=joints[index]

for i in range(np.shape(plot1)[1]):
#    plot1x.append(plot1.iloc[dex][i][0])
#    plot1y.append(plot1.iloc[dex][i][1])
#    plot1z.append(plot1.iloc[dex][i][2])
#    
#    plot2x.append(plot1.iloc[dex][i][0])
#    plot2y.append(plot1.iloc[dex][i][1])
#    plot2z.append(plot1.iloc[dex][i][2])
    dist.append(((plot1.iloc[dex][i][0])**2+(plot1.iloc[dex][i][1])**2+(plot1.iloc[dex][i][2])**2)**0.5)
    dist2.append(((plot2.iloc[dex][i][0])**2+(plot2.iloc[dex][i][1])**2+(plot2.iloc[dex][i][2])**2)**0.5)
    
 #   diff.append(dist[i]-dist2[i])
#######################################Below this should be a function but for now just do x

fig = plt.figure(figsize=(10, 5))
#fig, ax = plt.subplots()
plt.plot(dist)
plt.plot(dist2,"r")
#plt.hist(diff,len(diff))
plt.ylabel('Distance')
plt.xlabel('Frame')
plt.grid(True)
#ax.set_axisbelow(True)
#ax.minorticks_on()
#ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlim((0,102))
plt.show()



plt.tight_layout()
 

plt.show()