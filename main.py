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

data_f = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1_3d_data.json')
data_f_new = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1_3d_data.json')


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
#flat_bones = []
#for sublist in bones:
#    for item in sublist:
#        flat_bones.append(item)
#
#num_joints=len(Counter(flat_bones).keys())

##############################################################################
##############################################################################
#Initialise
    
frame=0
skeleton=[]
jeleton=[]
length=[]

for i in range(len(bones)):
    start=data_f[frame][bones[i][0]]
    end=data_f[frame][bones[i][1]]
    delta=np.subtract(end,start)
    delta_n=np.divide(delta,np.linalg.norm(delta)/limb_length[i])
    
    length.append(np.linalg.norm(delta))
    
    if i ==0:
        skeleton.append(cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta_n[0],delta_n[1],delta_n[2]), radius=20))
        data_f_new[frame][bones[i][1]]=np.add(start,delta_n)
    else:
        start=data_f_new[frame][bones[i][0]]
        skeleton.append(cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta_n[0],delta_n[1],delta_n[2]), radius=20))
#        if i in joints:
#            jeleton.append(sphere(pos=vector(endpoint[0],endpoint[1],endpoint[2]), radius=30))
        data_f_new[frame][bones[i][1]]=np.add(start,delta_n)
 
for i in range(len(joints)):
#    if i ==0:
#        jeleton.append(sphere(pos=vector(data_f[frame][bones[i][0]][0],data_f[frame][bones[i][0]][1],data_f[frame][bones[i][0]][2]), radius=30))
#    else:
    start=data_f_new[frame][joints[i]]
    jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30))
    
##############################################################################
##############################################################################
#Animation start

while frame<np.shape(data_f)[1]-1:

    sleep(0.02)
    frame+=1
    
    
    for i in range(len(bones)):
        start=data_f[frame][bones[i][0]]
        end=data_f[frame][bones[i][1]]
        delta=np.subtract(end,start)
        delta_n=np.divide(delta,np.linalg.norm(delta)/limb_length[i])
        
#        skeleton[i]=cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta[0],delta[1],delta[2]), radius=20)        
        start=data_f_new[frame][bones[i][0]]
        skeleton[i].pos=vector(start[0],start[1],start[2])
        skeleton[i].axis=vector(delta_n[0],delta_n[1],delta_n[2])
        data_f_new[frame][bones[i][1]]=np.add(start,delta_n)
 
    for i in range(len(joints)):
        start=data_f_new[frame][joints[i]]
        jeleton[i].pos=vector(start[0],start[1],start[2])
    
    


##############################################################################
##############################################################################    
#scene.width = scene.height = 800
#scene.range = 1.8
scene.title = "Pose Visualisation"   
#scene = canvas()