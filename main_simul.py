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


#    [0]  = 'Hip'   [1]  = 'RHip'   [2]  = 'RKnee'   [3]  = 'RFoot'   [6]  = 'LHip'   [7]  = 'LKnee'   [8]  = 'LFoot'   [12] = 'Spine'   [13] = 'Thorax'
#    [14] = 'Neck/Nose'   [15] = 'Head'   [17] = 'LShoulder'   [18] = 'LElbow'   [19] = 'LWrist'   [25] = 'RShoulder'   [26] = 'RElbow'   [27] = 'RWrist'

# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm

bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
limb_length=[124,452,504,124,452,504,252,231,78,112,120,250,230,120,250,230]


#formats data so that becomes matrix of dimensions. Rows are joints. Columns are frames. Also centres coords on hip
data_f = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1_3d_data.json',bones,joints,limb_length)
data_f_3= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3_3d_data.json',bones,joints,limb_length)
data_f_4= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4_3d_data.json',bones,joints,limb_length) 



    
frame=0

#scene1 = canvas()

    
#sim(frame,data_f,bones,joints,limb_length,vec(1,0,0))


#df_v=dt.df_v(data_f_new)
#df_a=dt.df_a(df_v)
#scene2 = canvas()
#sim(frame,data_f_3,bones,joints,limb_length,vec(0,0,1))


scene.camera.pos=vector(0,-2000,0)
scene.camera.axis=vector(0,+2000,0)
scene.up=vector(0,-1,0)
scene.userzoom =False
#scene.userspin=True
scene.width = scene.height = 1000
############################################################################

skeleton=[]
jeleton=[]

skeleton1=[]
jeleton1=[]

plot1=data_f
plot2=data_f_3.iloc[:,0:100]

while frame<max(np.shape(plot2)[1],np.shape(plot1)[1])-1:
    if frame<np.shape(plot1)[1]-1:
        temp=sim(skeleton,jeleton,frame,plot1,bones,joints,limb_length,vec(0,1,0))
        skeleton=temp[0]
        jeleton=temp[1]
    if frame<np.shape(plot2)[1]-1:     
        temp2=sim(skeleton1,jeleton1,frame,plot2,bones,joints,limb_length,vec(1,0,0))
        skeleton2=temp2[0]
        jeleton2=temp2[1]
        frame+=1


    frame+=1



#scene.range = 1.8
scene.title = "Pose Visualisation"   
