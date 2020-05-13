# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:11:03 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



import joint_angle as ja

def v4(index):
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
    
    #    #index mapping
    bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
        

     
    frames=np.shape(plot3)[1]
    #joint 0 to 27 Rwrist
    
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
    
    
    
#    plt.plot(angle1,"b",alpha=0.4)
#    plt.plot(angle2,"y",alpha=1)
#    plt.plot(angle3,"r",alpha=1) 
#    plt.plot(angle4,'b',alpha=0.4)
#    plt.plot(angle5,'orange',alpha=1)
#    plt.plot(angle6,'b',alpha=0.4)
#    #plt.plot(angle7,'b',alpha=0.4)
#    plt.plot(angle8,'b',alpha=0.4)
#    plt.plot(angle9,'b',alpha=0.4)
#    plt.plot(angle10,'b',alpha=0.4)
#  
#    plt.ylabel('Angle')
#    plt.xlabel('Frame')
#    plt.grid(True)
#
#    plt.xlim((0,140))
#    plt.show()
#    
#    
#    
#    plt.tight_layout()
     
    
    df = pd.DataFrame(np.array([angle1,angle2,angle3,angle4,angle5,angle6,angle7,angle8,angle9,angle10]))
    
    return df
    
#df=v4(1) #hip
#df=v4(4)
#df=v4(2) #knee
#df=v4(5)
#df=v4(3) #foot
#df=v4(6)
#df=v4(7) #spine
#df=v4(8) #thorax
#df=v4(9) #nose
#df=v4(10) #head
#df=v4(14) #shoulder
#df=v4(11) 
#df=v4(15) #arm
#df=v4(12)
#df=v4(16) #wrsit
#df=v4(13)