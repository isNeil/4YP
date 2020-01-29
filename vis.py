# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:22:35 2020

@author: neilw
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from colour import Color
import random

#plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3.json')
#plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5.json')
#plot1vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3vel.json')
#plot2vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5vel.json')
#plot1accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3accel.json')
#plot2accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5accel.json')

#    #index mapping
#    bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
#    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
    

def TimeColour3D(plot1,index,bones,joints):
    
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
                      
                      
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    red = Color("blue")
    colors = list(red.range_to(Color("green"),102))
    
    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)
    
    ax.scatter(plot1x, plot1y, plot1z, zdir='z', depthshade=True,alpha=0.9,c=rgbc)
    
    #make axis fit correctly
    xm=(max(plot1x)+min(plot1x))/2
    ym=(max(plot1y)+min(plot1y))/2
    zm=(max(plot1z)+min(plot1z))/2
    
    
    
    
    ax.scatter(plot1x, plot1y, [zm-600]*frames, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    ax.scatter([xm-600]*frames, plot1y, plot1z, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    ax.scatter(plot1x, [ym+600]*frames,  plot1z, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    
    ax.set_xlabel('X')
    ax.set_xlim(xm-600, xm+600)
    ax.set_ylabel('Y')
    ax.set_ylim(ym-600, ym+600)
    ax.set_zlabel('Z')
    ax.set_zlim(zm-600, zm+600)
    
    rngid=random.random()
    plt.savefig("%f.jpg"%rngid, dpi=60)    
    plt.show()
    return rngid
   
    


def Hagerstrand(plot1,index,bones,joints):
    
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
                      
                      
    fig = plt.figure(figsize=(25, 12.5))
    ax = fig.add_subplot(121, projection='3d')
    
    red = Color("blue")
    colors = list(red.range_to(Color("green"),102))
    
    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)
    
    ax.scatter((list(range(frames))), plot1y, plot1z, zdir='z', depthshade=True,alpha=0.9,c=rgbc)
    
    #make axis fit correctly
    xm=(max(plot1x)+min(plot1x))/2
    ym=(max(plot1y)+min(plot1y))/2
    zm=(max(plot1z)+min(plot1z))/2
    
    ax.scatter((list(range(frames))), plot1y, [zm-600]*frames, zdir='z',alpha=0.2,c=rgbc) #z)
    ax.scatter(-10, plot1y, plot1z, zdir='z',alpha=0.2,c=rgbc) #x)
    ax.scatter((list(range(frames))), [ym+600]*frames,  plot1z, zdir='z',alpha=0.2,c=rgbc) #y)
    
    ax.set_xlabel('X')
    ax.set_xlim(-10, frames+10)
    ax.set_ylabel('Y')
    ax.set_ylim(ym-600, ym+600)
    ax.set_zlabel('Z')
    ax.set_zlim(zm-600, zm+600)
    
    
    ######################################
    
    
    
    ax1= fig.add_subplot(122, projection='3d')
    ax1.scatter(plot1x, plot1y, (list(range(frames))), zdir='z', depthshade=True,alpha=0.9,c=rgbc)
    
 
    
    
    
    
    ax1.scatter([xm-600]*frames, plot1y, (list(range(frames))), zdir='z',alpha=0.2,c=rgbc) #x)
    ax1.scatter(plot1x, [ym+600]*frames,(list(range(frames))), zdir='z',alpha=0.2,c=rgbc) #y)
    ax1.scatter(plot1x, plot1y, -10, zdir='z',alpha=0.2,c=rgbc) #z
    
    ax1.set_xlabel('X')
    ax1.set_xlim(xm-600, xm+600)
    ax1.set_ylabel('Y')
    ax1.set_ylim(ym-600, ym+600)
    ax1.set_zlabel('Z')
    ax1.set_zlim(-10, frames+10)
    
    
    rngid=random.random()
    plt.tight_layout()
    plt.savefig("%f.jpg"%rngid, dpi=60)    
    
    plt.show()
    
    
    
    return rngid


