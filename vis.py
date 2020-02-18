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
import time
from v1f import v1
from v2f import v2
from v3f import v3
from v8f import v8
from v9f import v9
from v10f import v10
from v4f import v4

#plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3.json')
#plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5.json')
#plot1vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3vel.json')
#plot2vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5vel.json')
#plot1accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3accel.json')
#plot2accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5accel.json')

#    #index mapping
#    bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
#    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
    

def TimeColour3DJ(plot1,index,bones,joints,graph_id):
 
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
                                      
    fig = plt.figure(figsize=(12.5, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    red = Color("blue")
    colors = list(red.range_to(Color("green"),102))
    
    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)
    
    #make axis fit correctly
    xm=(max(plot1x)+min(plot1x))/2
    ym=(max(plot1y)+min(plot1y))/2
    zm=(max(plot1z)+min(plot1z))/2
    
    ax.scatter(plot1x, plot1y, plot1z, zdir='z', depthshade=True,alpha=0.9,c=rgbc)
    ax.scatter(plot1x, plot1y, [zm-600]*frames, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    ax.scatter([xm-600]*frames, plot1y, plot1z, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    ax.scatter(plot1x, [ym+600]*frames,  plot1z, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    
    ax.set_xlabel('X')
    ax.set_xlim(xm-600, xm+600)
    ax.set_ylabel('Y')
    ax.set_ylim(ym-600, ym+600)
    ax.set_zlabel('Z')
    ax.set_zlim(zm-600, zm+600)
    plt.tight_layout()

    plt.savefig("graph%d.jpg"%graph_id, dpi=60)  
    
    plt.show()
    
    
def TimeColour3DS(plot1,index,bones,joints,graph_id):

    frames=np.shape(plot1)[1]
    #joint 0 to 27 Rwrist
    plot1x=[]
    plot1y=[]
    plot1z=[]
    x=[]
    y=[]
    z=[]
    #mapping index to bones to find joint number
    dex=bones[index][0]
    dex_prev=bones[index][1]
    
    for i in range(np.shape(plot1)[1]):
        plot1x.append(plot1.iloc[dex][i][0])
        plot1y.append(plot1.iloc[dex][i][1])
        plot1z.append(plot1.iloc[dex][i][2])
        x.append(plot1.iloc[dex_prev][i][0])
        y.append(plot1.iloc[dex_prev][i][1])
        z.append(plot1.iloc[dex_prev][i][2])
                                  
    fig = plt.figure(figsize=(12.5, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    red = Color("blue")
    colors = list(red.range_to(Color("green"),102))
    
    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)

    #make axis fit correctly
    xm=(max(plot1x)+min(plot1x))/2
    ym=(max(plot1y)+min(plot1y))/2
    zm=(max(plot1z)+min(plot1z))/2
    

    for i in range(frames):
        ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[plot1z[i],z[i]], color=rgbc[i])
        ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[zm-600,zm-600],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([xm-600,xm-600], [plot1y[i],y[i]], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([plot1x[i],x[i]], [ym+600,ym+600], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)

    ax.set_xlabel('X')
    ax.set_xlim(xm-600, xm+600)
    ax.set_ylabel('Y')
    ax.set_ylim(ym-600, ym+600)
    ax.set_zlabel('Z')
    ax.set_zlim(zm-600, zm+600)
    plt.tight_layout()

    plt.savefig("graph%d.jpg"%graph_id, dpi=60)  

    plt.show()

def TC3DLimb(plot1,index,bones,joints,graph_id):
    #take joint in between bones
    
    frames=np.shape(plot1)[1]
    #mapping index to bones to find joint number
    
    
    
    dex=joints[index]
    dex_prev=joints[index-1]
    dex_post=joints[index+1]
    #check it actually is a limb joint by saying limbs are sequential numbers- bit of a gimmicky method- MOVED INTO menu 
    
    print(dex)
    print(dex_prev)
    print(dex_post)
    
    plot1x=[]
    plot1y=[]
    plot1z=[]
    x=[]
    y=[]
    z=[]
    x1=[]
    y1=[]
    z1=[]
    
    for i in range(np.shape(plot1)[1]):
        plot1x.append(plot1.iloc[dex_post][i][0])
        plot1y.append(plot1.iloc[dex_post][i][1])
        plot1z.append(plot1.iloc[dex_post][i][2])
        x.append(plot1.iloc[dex][i][0])
        y.append(plot1.iloc[dex][i][1])
        z.append(plot1.iloc[dex][i][2])
        x1.append(plot1.iloc[dex_prev][i][0])
        y1.append(plot1.iloc[dex_prev][i][1])
        z1.append(plot1.iloc[dex_prev][i][2])                  
                      
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    #ax.view_init(20, 200)
    red = Color("blue")
    colors = list(red.range_to(Color("green"),102))
    
    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)
        
    #make axis fit correctly
    xm=(max(x)+min(x))/2
    ym=(max(y)+min(y))/2
    zm=(max(z)+min(z))/2
    
    for i in range(frames):
        
        ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[plot1z[i],z[i]], color=rgbc[i])
        ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[zm-600,zm-600],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([xm-600,xm-600], [plot1y[i],y[i]], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([plot1x[i],x[i]], [ym+600,ym+600], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        
        ax.plot([x[i],x1[i]],[y[i],y1[i]],[z[i],z1[i]], color=rgbc[i])
        ax.plot([x[i],x1[i]],[y[i],y1[i]],[zm-600,zm-600],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([xm-600,xm-600], [y[i],y1[i]], [z[i],z1[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([x[i],x1[i]], [ym+600,ym+600], [z[i],z1[i]],color=rgbc[i],alpha=0.2) #cmap=cm.c
   
    ax.set_xlabel('X')
    ax.set_xlim(-700, 700)
    ax.set_ylabel('Y')
    ax.set_ylim(-700, 700)
    ax.set_zlabel('Z')
    ax.set_zlim(-400, 1000)   
    
    plt.tight_layout()
    plt.savefig("graph%d.jpg"%graph_id, dpi=60)    
    
    plt.show()
    
def Hagerstrand(plot1,index,bones,joints,graph_id):
    
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
                                           
    fig = plt.figure(figsize=(25, 10))
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
        

    plt.tight_layout()
    plt.savefig("graph%d.jpg"%graph_id, dpi=60)    
    
    plt.show()
        
def plotpositionalderivatives(index,bones,joints):
    
    fig, axs = plt.subplots(4,2,figsize=(20, 10))
   
    
    df=v1(index)
    axs[0,0].plot(df.iloc[0,:],'r')
    axs[0,0].plot(df.iloc[1,:],'b',alpha=0.4)
    axs[0,0].plot(df.iloc[2,:],'b',alpha=0.4)
    axs[0,0].plot(df.iloc[3,:],'b',alpha=0.4)
    axs[0,0].plot(df.iloc[4,:],'b',alpha=0.4)
    axs[0,0].plot(df.iloc[5,:],'b',alpha=0.4)
    axs[0,0].plot(df.iloc[6,:],'b',alpha=0.4)
    axs[0,0].plot(df.iloc[7,:],'b',alpha=0.4)
    axs[0,0].set_ylabel('Distance')
    axs[0,0].set_xlabel('Frame')
    
    df=v2(index)
    axs[1,0].plot(df.iloc[0,:],'r')
    axs[1,0].plot(df.iloc[1,:],'b',alpha=0.4)
    axs[1,0].plot(df.iloc[2,:],'b',alpha=0.4)
    axs[1,0].plot(df.iloc[3,:],'b',alpha=0.4)
    axs[1,0].plot(df.iloc[4,:],'b',alpha=0.4)
    axs[1,0].plot(df.iloc[5,:],'b',alpha=0.4)
    axs[1,0].plot(df.iloc[6,:],'b',alpha=0.4)
    axs[1,0].plot(df.iloc[7,:],'b',alpha=0.4)
    axs[1,0].set_ylabel('Velocity')
    axs[1,0].set_xlabel('Frame')    
    
    df=v3(index)
    axs[2,0].plot(df.iloc[0,:],'r')
    axs[2,0].plot(df.iloc[1,:],'b',alpha=0.4)
    axs[2,0].plot(df.iloc[2,:],'b',alpha=0.4)
    axs[2,0].plot(df.iloc[3,:],'b',alpha=0.4)
    axs[2,0].plot(df.iloc[4,:],'b',alpha=0.4)
    axs[2,0].plot(df.iloc[5,:],'b',alpha=0.4)
    axs[2,0].plot(df.iloc[6,:],'b',alpha=0.4)
    axs[2,0].plot(df.iloc[7,:],'b',alpha=0.4)   
    axs[2,0].set_ylabel('Acceleration')
    axs[2,0].set_xlabel('Frame')
    
    df=v8(index)
    axs[0,1].plot(df.iloc[0,:],'r')
    axs[0,1].plot(df.iloc[1,:],'b',alpha=0.4)
    axs[0,1].plot(df.iloc[2,:],'b',alpha=0.4)
    axs[0,1].plot(df.iloc[3,:],'b',alpha=0.4)
    axs[0,1].plot(df.iloc[4,:],'b',alpha=0.4)
    axs[0,1].plot(df.iloc[5,:],'b',alpha=0.4)
    axs[0,1].plot(df.iloc[6,:],'b',alpha=0.4)
    axs[0,1].plot(df.iloc[7,:],'b',alpha=0.4)   
    axs[0,1].set_ylabel('Distance')
    axs[0,1].set_xlabel('Frame')   
    
    df=v9(index)
    axs[1,1].plot(df.iloc[0,:],'r')
    axs[1,1].plot(df.iloc[1,:],'b',alpha=0.4)
    axs[1,1].plot(df.iloc[2,:],'b',alpha=0.4)
    axs[1,1].plot(df.iloc[3,:],'b',alpha=0.4)
    axs[1,1].plot(df.iloc[4,:],'b',alpha=0.4)
    axs[1,1].plot(df.iloc[5,:],'b',alpha=0.4)
    axs[1,1].plot(df.iloc[6,:],'b',alpha=0.4)
    axs[1,1].plot(df.iloc[7,:],'b',alpha=0.4)   
    axs[1,1].set_ylabel('Velocity')
    axs[1,1].set_xlabel('Frame')   
        
    df=v10(index)
    axs[2,1].plot(df.iloc[0,:],'r')
    axs[2,1].plot(df.iloc[1,:],'b',alpha=0.4)
    axs[2,1].plot(df.iloc[2,:],'b',alpha=0.4)
    axs[2,1].plot(df.iloc[3,:],'b',alpha=0.4)
    axs[2,1].plot(df.iloc[4,:],'b',alpha=0.4)
    axs[2,1].plot(df.iloc[5,:],'b',alpha=0.4)
    axs[2,1].plot(df.iloc[6,:],'b',alpha=0.4)
    axs[2,1].plot(df.iloc[7,:],'b',alpha=0.4)   
    axs[2,1].set_ylabel('Acceleration')
    axs[2,1].set_xlabel('Frame')   


    df=v4(15)
    axs[3,0].plot(df.iloc[0,:],'r')
    axs[3,0].plot(df.iloc[1,:],'b',alpha=0.4)
    axs[3,0].plot(df.iloc[2,:],'b',alpha=0.4)
    axs[3,0].plot(df.iloc[3,:],'b',alpha=0.4)
    axs[3,0].plot(df.iloc[4,:],'b',alpha=0.4)
    axs[3,0].plot(df.iloc[5,:],'b',alpha=0.4)
    axs[3,0].plot(df.iloc[6,:],'b',alpha=0.4)
    axs[3,0].plot(df.iloc[7,:],'b',alpha=0.4)   
    axs[3,0].set_ylabel('Angle')
    axs[3,0].set_xlabel('Frame')   

    fig.tight_layout()
    plt.savefig("std_pos_vis%d.jpg"%index, dpi=60)    
    

bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
plotpositionalderivatives(16,bones,joints)
