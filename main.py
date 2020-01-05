# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:45:43 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np
from formatdata import format


data_f = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1_3d_data.json')

frame=100
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
# 1.R pelvis 2.R femur 3.R tibia 4.L pelvis 5.L femur 6.L tibia 7.lowerback 8.upperback 9.neck 10.head 11.L clavicle 
# 10.head  11.L clavicle 12.L upperarm 13.L lowerarm 14.R clav 15.R up arm 16.R low arm
bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27],[14,15]];



#[skeleton{bones(i,1),x}(1),skeleton{bones(i,2),x}(1)],[skeleton{bones(i,1),x}(2),skeleton{bones(i,2),x}(2)],[skeleton{bones(i,1),x}(3),skeleton{bones(i,2),x}(3)])

for i in range(len(bones)):
    start=data_f[frame][bones[i][0]]
    end=data_f[frame][bones[i][1]]
    delta=np.subtract(end,start)
    
    rod = cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta[0],delta[1],delta[2]), radius=30)

scene.width = scene.height = 800
#scene.range = 1.8
scene.title = "Pose Visualisation"   
scene = canvas()