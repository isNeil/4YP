# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 01:41:30 2020

@author: neilw
"""
import numpy as np
import math
from formatdata_length_constraint import format



def length(v):
  return (np.dot(v, v))**0.5

def angle(v1, v2):
  return math.acos(np.dot(v1, v2) / (length(v1) * length(v2)))

def joint_angle(frame,df,bones,joints):

    
    #all bones at joint
    angles=[[] for i in range(len(joints))]
    
    for x in range(len(joints)):
        for i in range(len(bones)):
            if joints[x] in bones[i]:
                angles[x].append(i)
    
    
    
    bone_v=[]
    for x in range(len(bones)):
        bone_v.append(np.subtract(df[frame][bones[x][1]],df[frame][bones[x][0]]))
    
    joint_a=[0]*len(joints)
    for i in range(len(angles)):
        if len(angles[i])==2:
            joint_a[i]=math.degrees(angle(bone_v[angles[i][0]],bone_v[angles[i][1]]))
    
    return joint_a
           
#bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
#joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
#limb_length=[124,452,504,124,452,504,252,231,78,112,120,250,230,120,250,230]
#data_f_4= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4_3d_data.json',bones,joints,limb_length) 
#a=joint_angle(0,data_f_4,bones,joints)




        
    