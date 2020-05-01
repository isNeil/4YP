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

def v5(index):

    plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\1.json')
    plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\2.json')
    plot3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\3.json')
    plot4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\4.json')
    plot5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\5.json')
    plot6= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\6.json')
    plot7= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\7.json')
    plot8= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\8.json')
    plot9= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\9.json')
    plot10= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\10.json')
    
    frames=np.shape(plot1)[1]
    #    #index mapping
    bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
        
    angle1=[]
    angle2=[]
    angle3=[]
    angle4=[]
    angle5=[]
    angle6=[]
    angle7=[]
    angle8=[]
    angle9=[]
    angle10=[]
    
    
    
    
    #mapping index to joint 

    
    for i in range(frames):
        #ja.joint_angle(i,plot3,bones,joints)
        angle1.append(ja.joint_angle(i,plot1,bones,joints)[index])
        angle2.append(ja.joint_angle(i,plot2,bones,joints)[index])
        angle3.append(ja.joint_angle(i,plot3,bones,joints)[index]) #ja.joint_angle returns angles for entire skeleton so select joint using index
        angle4.append(ja.joint_angle(i,plot4,bones,joints)[index])
        angle5.append(ja.joint_angle(i,plot5,bones,joints)[index])
        angle6.append(ja.joint_angle(i,plot6,bones,joints)[index])
        angle7.append(ja.joint_angle(i,plot7,bones,joints)[index])
        angle8.append(ja.joint_angle(i,plot8,bones,joints)[index])
        angle9.append(ja.joint_angle(i,plot9,bones,joints)[index])
        angle10.append(ja.joint_angle(i,plot10,bones,joints)[index])
    

   #######################################Below this should be a function but for now just do x
    #dist = savgol_filter(dist, 21, 3) # window size 51, polynomial order 3
    dist1 = savgol_filter(angle1, 21, 3)
    dist2 = savgol_filter(angle2, 21, 3)  
    dist3 = savgol_filter(angle3, 21, 3)  
    dist4 = savgol_filter(angle4, 21, 3)  
    dist5 = savgol_filter(angle5, 21, 3)  
    dist6 = savgol_filter(angle6, 21, 3)  
    dist7 = savgol_filter(angle7, 21, 3)  
    dist8 = savgol_filter(angle8, 21, 3)  
    dist9 = savgol_filter(angle9, 21, 3)  
    dist10 = savgol_filter(angle10, 21, 3)  

    temp1=[]
    temp2=[]
    temp3=[]
    temp4=[]
    temp5=[]
    temp6=[]
    temp7=[]
    temp8=[]
    temp9=[]
    temp10=[]
    
    for i in range(frames-1):
        
        temp1.append(dist1[i+1]-dist1[i])
        temp2.append(dist2[i+1]-dist2[i])
        temp3.append(dist3[i+1]-dist3[i])
        temp4.append(dist4[i+1]-dist4[i])
        temp5.append(dist5[i+1]-dist5[i])
        temp6.append(dist6[i+1]-dist6[i])
        temp7.append(dist7[i+1]-dist7[i])
        temp8.append(dist8[i+1]-dist8[i])
        temp9.append(dist9[i+1]-dist9[i])
        temp10.append(dist10[i+1]-dist10[i])
            
        
    
    
    
#    plt.plot(temp1,"b",alpha=0.4)
#    plt.plot(temp2,"yellow",alpha=1)
#    plt.plot(temp3,"red",alpha=1) 
#    plt.plot(temp4,'b',alpha=0.4)
#    plt.plot(temp5,'orange',alpha=1)
#    plt.plot(temp6,'b',alpha=0.4)
#   # plt.plot(temp7,'b',alpha=0.4)
#    plt.plot(temp8,'b',alpha=0.4)
#    plt.plot(temp9,'b',alpha=0.4)
#    plt.plot(temp10,'b',alpha=0.4)
#  
#    plt.ylabel('Velocity')
#    plt.xlabel('Frame')
#    plt.grid(True)
#
#    plt.xlim((0,140))
#    plt.show()
#    
#    
#    
#    plt.tight_layout()
     
    df = pd.DataFrame(np.array([temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,temp10]))
    
    return df




