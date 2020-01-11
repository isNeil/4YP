# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:45:43 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np
from formatdata_length_constraint import format
from collections import Counter
from scipy import signal
from simulation_simul import sim
import matplotlib.pyplot as plt
import calc_vel_accel as dt
import joint_angle as ja
import math
from colour import Color
import joint_angle as ja


#    [0]  = 'Hip'   [1]  = 'RHip'   [2]  = 'RKnee'   [3]  = 'RFoot'   [6]  = 'LHip'   [7]  = 'LKnee'   [8]  = 'LFoot'   [12] = 'Spine'   [13] = 'Thorax'
#    [14] = 'Neck/Nose'   [15] = 'Head'   [17] = 'LShoulder'   [18] = 'LElbow'   [19] = 'LWrist'   [25] = 'RShoulder'   [26] = 'RElbow'   [27] = 'RWrist'

# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm

bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
limb_length=[124,452,504,124,452,504,252,231,78,112,120,250,230,120,250,230]


#formats data so that becomes matrix of dimensions. Rows are joints. Columns are frames. Also centres coords on hip
#data_f = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1_3d_data.json',bones,joints,limb_length)
#data_f.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1formated.json')
#data_f_3= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3_3d_data.json',bones,joints,limb_length)
#data_f_3.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
#data_f_4= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4_3d_data.json',bones,joints,limb_length) 
#data_f_4.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4formated.json')
#data_f_5= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5_3d_data.json',bones,joints,limb_length) 
#data_f_5.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')


#load formated data instead
data_f = pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1formated.json')
data_f_3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
data_f_4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4formated.json')  
data_f_5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')  


frame=0

#df_v=dt.df_v(data_f_new)
#df_a=dt.df_a(df_v)
#scene2 = canvas()
#sim(frame,data_f_3,bones,joints,limb_length,vec(0,0,1))

scene=canvas()
scene.camera.pos=vector(1,-2000,0)
scene.camera.axis=vector(-1,+2000,0)
scene.up=vector(0,0,1)
scene.userzoom =False
scene.userspin=True
scene.width = scene.height = 1000
############################################################################

skeleton=[]
jeleton=[]

skeleton1=[]
jeleton1=[]

#plot1=data_f
#plot2=data_f_4.iloc[:,15:117]
#plot2.columns = range(plot2.shape[1])

plot1=data_f_3.iloc[:,40:142]
plot1.columns = range(plot1.shape[1])
#plot1=data_f_4.iloc[:,10:112]
#plot1.columns = range(plot2.shape[1])

#plot2=data_f_3.iloc[:,70:172]
#plot2.columns = range(plot1.shape[1])

plot2=data_f_5.iloc[:,25:127]
plot2.columns = range(plot2.shape[1])
d_lines=[]

while frame<max(np.shape(plot2)[1],np.shape(plot1)[1])-1:
    if frame<np.shape(plot1)[1]-1:
        temp=sim(skeleton,jeleton,frame,plot1,bones,joints,limb_length,vec(0,1,0))
        skeleton=temp[0]
        jeleton=temp[1]
    if frame<np.shape(plot2)[1]-1:     
        temp2=sim(skeleton1,jeleton1,frame,plot2,bones,joints,limb_length,vec(1,0,0))
        skeleton1=temp2[0]
        jeleton1=temp2[1]
        
    
    start=plot1[frame]
    end=plot2[frame]
    delta=np.subtract(end[joints[-1]],start[joints[-1]])
    start_temp=start[joints[-1]]
    
    d_lines.append(cylinder(pos=vector(start_temp[0],start_temp[1],start_temp[2]), axis=vector(delta[0],delta[1],delta[2]), radius=2, color=vec(0,0,1)))

    #joint angle colouring

    angles1=ja.joint_angle(frame,plot1,bones,joints)  
    angles2=ja.joint_angle(frame,plot2,bones,joints) 
    angles=np.subtract(angles1,angles2)
    #print(max(angles))
    
    red = Color("yellow")
    colors = list(red.range_to(Color("red"),70))
    
    for i in range(len(jeleton)):
        if angles[i]==0:
            jeleton[i].color=color.white
        else:
            rgbc=colors[abs(int(angles[i]))].rgb
            jeleton[i].color=vector(rgbc[0],rgbc[1],rgbc[2])

    #label right arm angle 
    start_temp=start[joints[-2]]
    
    if frame ==0:
        al=label(pos=vec(start_temp[0],start_temp[1],start_temp[2]), text=int(angles1[15]), yoffset=-50)
        
    else:
        
        al.pos=vec(start_temp[0],start_temp[1],start_temp[2])
        al.text=angles1[15]
    

    #graph
    f1 = gdots(color=color.cyan)
    f1.plot(pos=[frame,angles1[15]])
    f2 = gdots(color=color.magenta)
    f2.plot(pos=[frame,angles2[15]])
    frame+=1


#scene.range = 1.8
scene.title = "Pose Visualisation"   
