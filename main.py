# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:45:43 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np
from formatdata import format
from collections import Counter
from scipy import signal
from simulation import sim
import matplotlib.pyplot as plt
import calc_vel_accel as dt

data_f = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1_3d_data.json')

#data_f_3= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3_3d_data.json') 
#data_f_4= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4_3d_data.json') 

#    % H36M_NAMES[0]  = 'Hip'
#    % H36M_NAMES[1]  = 'RHip'
#    % H36M_NAMES[2]  = 'RKnee'
#    % H36M_NAMES[3]  = 'RFoot'
#    % H36M_NAMES[6]  = 'LHip'
#    % H36M_NAMES[7]  = 'LKnee'
#    % H36M_NAMES[8]  = 'LFoot'
#    % H36M_NAMES[12] = 'Spine'
#    % H36M_NAMES[13] = 'Thorax'
#    % H36M_NAMES[14] = 'Neck/Nose'
#    % H36M_NAMES[15] = 'Head'
#    % H36M_NAMES[17] = 'LShoulder'
#    % H36M_NAMES[18] = 'LElbow'
#    % H36M_NAMES[19] = 'LWrist'
#    % H36M_NAMES[25] = 'RShoulder'
#    % H36M_NAMES[26] = 'RElbow'
#    % H36M_NAMES[27] = 'RWrist'
# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm
bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
limb_length=[124,452,504,124,452,504,252,231,78,112,120,250,230,120,250,230]

    
frame=0
data_f_new=sim(frame,data_f,bones,joints,limb_length,vec(1,0,0))

df_v=dt.df_v(data_f_new)
df_a=dt.df_a(df_v)

#data_f_new_3=sim(frame,data_f_3,bones,joints,limb_length,vec(0,0,1))


#data_f_new_4=sim(frame,data_f_4,bones,joints,limb_length,vec(0,1,0))


#def list_coords(joint,axis,data):    
#    list=[]
#    for i in range(len(data)):
#        list.append(data[i][joint][axis])
#    return list
#
#x1=list_coords(31,0,data_f_new)
#y1=list_coords(31,1,data_f_new)
#z1=list_coords(31,2,data_f_new)
#x3=list_coords(31,0,data_f_new_3)
#y3=list_coords(31,1,data_f_new_3)
#z3=list_coords(31,2,data_f_new_3)



#scene.width = scene.height = 800
#scene.range = 1.8
scene.title = "Pose Visualisation"   
#scene = canvas()