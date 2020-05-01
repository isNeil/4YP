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

def v4(index):
    plot3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\3.json')
    plot4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\4.json')
    plot5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\5.json')
    plot6= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\6.json')
    plot7= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\7.json')
    plot8= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\8.json')
    plot9= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\9.json')
    plot10= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\10.json')
    
    
    #    #index mapping
    bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
        

     
    frames=np.shape(plot3)[1]
    #joint 0 to 27 Rwrist
    
    angle3=[]
    angle4=[]
    angle5=[]
    angle6=[]
    angle7=[]
    angle8=[]
    angle9=[]
    angle10=[]
    
    
    
    
    
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

    
    for i in range(frames):
        #ja.joint_angle(i,plot3,bones,joints)
        angle3.append(ja.joint_angle(i,plot3,bones,joints)[index]) #ja.joint_angle returns angles for entire skeleton so select joint using index
        angle4.append(ja.joint_angle(i,plot4,bones,joints)[index])
        angle5.append(ja.joint_angle(i,plot5,bones,joints)[index])
        angle6.append(ja.joint_angle(i,plot6,bones,joints)[index])
        angle7.append(ja.joint_angle(i,plot7,bones,joints)[index])
        angle8.append(ja.joint_angle(i,plot8,bones,joints)[index])
        angle9.append(ja.joint_angle(i,plot9,bones,joints)[index])
        angle10.append(ja.joint_angle(i,plot10,bones,joints)[index])
    
    
        
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
    
    df = pd.DataFrame(np.array([angle3,angle4,angle5,angle6,angle7,angle8,angle9,angle10]))
    
    return df
    
#    fig = plt.figure(figsize=(10, 5))
#    #fig, ax = plt.subplots()
#    
#    plt.plot(angle3,"r")
#    plt.plot(angle4,'b')
#    plt.plot(angle5,'y')
#    plt.plot(angle6,'orange')
#    plt.plot(angle7,'purple')
#    plt.plot(angle8,'g')
#    plt.plot(angle9,'black')
#    plt.plot(angle10,'grey')
#    
#    
#    
#    plt.ylabel('Angle')
#    plt.xlabel('Frame')
#    plt.grid(True)
#    #ax.set_axisbelow(True)
#    #ax.minorticks_on()
#    #ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
#    plt.xlim((0,102))
#    plt.show()
#    
#    
#    
#    plt.tight_layout()
#     
#    
#    plt.show()