# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:45:43 2020

@author: neilw
"""
from vpython import *
import pandas as pd


#    [0]  = 'Hip'   [1]  = 'RHip'   [2]  = 'RKnee'   [3]  = 'RFoot'   [6]  = 'LHip'   [7]  = 'LKnee'   [8]  = 'LFoot'   [12] = 'Spine'   [13] = 'Thorax'
#    [14] = 'Neck/Nose'   [15] = 'Head'   [17] = 'LShoulder'   [18] = 'LElbow'   [19] = 'LWrist'   [25] = 'RShoulder'   [26] = 'RElbow'   [27] = 'RWrist'

# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm

bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
limb_length=[124,452,504,124,452,504,252,231,78,112,120,250,230,120,250,230]


#formats data so that becomes matrix of dimensions. Rows are joints. Columns are frames. Also centres coords on hip
data_f = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\jump1\3d_data.json',bones,joints,limb_length)
data_f.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1formated.json')
data_f_3= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3_3d_data.json',bones,joints,limb_length)
data_f_3.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
data_f_4= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4_3d_data.json',bones,joints,limb_length) 
data_f_4.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4formated.json')
data_f_5= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5_3d_data.json',bones,joints,limb_length) 
data_f_5.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')


#load formated data instead
#data_f = pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1formated.json')
#data_f_3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
#data_f_4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4formated.json')  
#data_f_5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')  



