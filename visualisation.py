# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:52:35 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from matplotlib import cm
#from matplotlib.pyplot import savefig
from colour import Color

plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3.json')
plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5.json')
#plot1vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3vel.json')
#plot2vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5vel.json')
#plot1accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3accel.json')
#plot2accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5accel.json')
frames=np.shape(plot1)[1]
#joint 0 to 27 Rwrist

plot1x=[]
plot1y=[]
plot1z=[]
x=[]
y=[]
z=[]
for i in range(np.shape(plot1)[1]):
    plot1x.append(plot1.iloc[27][i][0])
    plot1y.append(plot1.iloc[27][i][1])
    plot1z.append(plot1.iloc[27][i][2])
    x.append(plot1.iloc[26][i][0])
    y.append(plot1.iloc[26][i][1])
    z.append(plot1.iloc[26][i][2])
                  
                  
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

red = Color("blue")
colors = list(red.range_to(Color("green"),102))

rgbc=[]
for i in colors:
    rgbc.append(i.rgb)
for i in range(100):
    ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[plot1z[i],z[i]], color=rgbc[i])

    ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[-400,-400],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
    ax.plot([-700,-700], [plot1y[i],y[i]], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
    ax.plot([plot1x[i],x[i]], [700,700], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-700, 700)
ax.set_ylabel('Y')
ax.set_ylim(-700, 700)
ax.set_zlabel('Z')
ax.set_zlim(-400, 1000)
################################################################################
#frames=np.shape(plot1)[1]
#
#
#red = Color("blue")
#colors = list(red.range_to(Color("green"),102))
#
#rgbc=[]
#for i in colors:
#    rgbc.append(i.rgb)
#
#ax.scatter( list(range(frames)), plot1y, plot1z, zdir='z', depthshade=True,alpha=0.9,c=rgbc)
#
#
###
##ax.scatter(plot1x, plot1y, [-10]*frames, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
##ax.scatter([-700]*frames, plot1y, list(range(frames)), zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
##ax.scatter(plot1x, [700]*frames,  list(range(frames)), zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
##
##ax.set_xlabel('X')
##ax.set_xlim(-700, 700)
##ax.set_ylabel('Y')
##ax.set_ylim(-700, 700)
##ax.set_zlabel('Z')
##ax.set_zlim(-10, 105)
#
#ax.scatter(list(range(frames)), plot1y, [-400]*frames, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
#ax.scatter([-10]*frames, plot1y, plot1z, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
#ax.scatter(list(range(frames)), [700]*frames,  plot1z, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
#
#ax.set_xlabel('X')
#ax.set_xlim(-10, 105)
#ax.set_ylabel('Y')
#ax.set_ylim(-700, 700)
#ax.set_zlabel('Z')
#ax.set_zlim(-400, 1000)

###############################################################################
#frames=np.shape(plot1)[1]
#
#red = Color("blue")
#colors = list(red.range_to(Color("green"),102))
#
#rgbc=[]
#for i in colors:
#    rgbc.append(i.rgb)
#
#ax.plot(list(range(frames)), plot1y,plot1z , zdir='z',alpha=0.9,c='blue', lw=2)
#
#ax.plot(list(range(frames)), plot1y, [-400]*frames, zdir='z',alpha=0.2,c='blue',lw=2) #cmap=cm.coolwarm)
#ax.plot([-10]*frames, plot1y, plot1z, zdir='z',alpha=0.2,c='blue',lw=2) #cmap=cm.coolwarm)
#ax.plot(list(range(frames)), [700]*frames,  plot1z, zdir='z',alpha=0.2,c='blue',lw=2) #cmap=cm.coolwarm)
#
#ax.set_xlabel('X')
#ax.set_xlim(-10, 105)
#ax.set_ylabel('Y')
#ax.set_ylim(-700, 700)
#ax.set_zlabel('Z')
#ax.set_zlim(-400, 1000)
#
plt.show()

#plt.savefig('plot1.png', dpi=None)