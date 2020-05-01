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

def v11(index):
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
    
    angle4=np.subtract(angle4,angle3)
    angle5=np.subtract(angle5,angle3)
    angle6=np.subtract(angle6,angle3)
    angle7=np.subtract(angle7,angle3)
    angle8=np.subtract(angle8,angle3)
    angle9=np.subtract(angle9,angle3)
    angle10=np.subtract(angle10,angle3)
    angle3=np.subtract(angle3,angle3)
    
    
    
    df = pd.DataFrame(np.array([angle3,angle4,angle5,angle6,angle7,angle8,angle9,angle10]))
    
    return df
    