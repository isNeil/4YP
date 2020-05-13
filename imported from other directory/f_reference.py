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
#plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5.json')
#plot1vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3vel.json')
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


#make axis fit correctly
xm=(max(plot1x)+min(plot1x))/2
ym=(max(plot1y)+min(plot1y))/2
zm=(max(plot1z)+min(plot1z))/2



                                  
fig = plt.figure(figsize=(12.5, 10))

ax = fig.add_subplot(311)
ay = fig.add_subplot(312)  
az = fig.add_subplot(313) 

#red = Color("blue")
#colors = list(red.range_to(Color("green"),102))

#rgbc=[]
#for i in colors:
#    rgbc.append(i.rgb)

ax.plot(plot1x,'bo')
plt.ylabel('Displacement x')
plt.xlabel('Frame')
plt.grid(True)
plt.xlim((0,102))



#ay.plot(plot1y,'bo')
#plt.ylabel('Displacement y')
#plt.xlabel('Frame')
#plt.grid(True)
#plt.xlim((0,102))
#
#
#
#az.plot(plot1x,'bo')
#plt.ylabel('Displacement z')
#plt.xlabel('Frame')
#plt.grid(True)
#plt.xlim((0,102))

# Major ticks every 20, minor ticks every 5
#major_ticks = np.arange(-1000, 1000, 50)
#minor_ticks = np.arange(0, 101, 5)
#
#ax.set_xticks(major_ticks)
#ax.set_xticks(minor_ticks, minor=True)
#ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor=True)

# And a corresponding grid
ax.grid(which='both')


plt.show()



#ax.set_xlabel('X')
#ax.set_xlim(xm-600, xm+600)
#ax.set_ylabel('Y')
#ax.set_ylim(ym-600, ym+600)
#ax.set_zlabel('Z')
#ax.set_zlim(zm-600, zm+600)
plt.tight_layout()

   #plt.savefig("graph%d.jpg"%graph_id, dpi=60)  

plt.show()