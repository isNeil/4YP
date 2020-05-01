# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:23:03 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np
import joint_angle as ja
from collections import Counter
import scipy
from colour import Color
# plot trails 
def ghost(skeleton,jeleton,frame,data_f,bones,joints,limb_length,trace_colour,vis=True,ball=True,col=vec(1,1,1)):):

    k=20
    skeleton=[]
      
    if frame%k==0:
        for i in range(len(bones)):
            
            start=data_f[frame][bones[i][0]]
            end=data_f[frame][bones[i][1]]
            delta=np.subtract(end,start)
            delta=np.divide(delta,np.linalg.norm(delta)/limb_length[i])
    
    #                length.append(np.linalg.norm(delta))
    
            if i ==0:
                skeleton.append(cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta[0],delta[1],delta[2]), radius=20, opacity=1))
                data_f_new[frame][bones[i][1]]=np.add(start,delta)
            else:
    
                start=data_f_new[frame][bones[i][0]]
                skeleton.append(cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta[0],delta[1],delta[2]), radius=20, opacity=1))
    
    #        if i in joints:
    #            jeleton.append(sphere(pos=vector(endpoint[0],endpoint[1],endpoint[2]), radius=30))
                data_f_new[frame][bones[i][1]]=np.add(start,delta)
     
        for i in range(len(joints)):
    #    if i ==0:
    #        jeleton.append(sphere(pos=vector(data_f[frame][bones[i][0]][0],data_f[frame][bones[i][0]][1],data_f[frame][bones[i][0]][2]), radius=30))
    #    else:
            start=data_f_new[frame][joints[i]]
            jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30, opacity= 1))
        for j in range(len(skeleton)):
            
            skeleton[j].opacity+=-0.1
            if skeleton[j].opacity<=0.2:
                skeleton[j].opacity=0.2
            
          
        for l in range(len(jeleton)):
            jeleton[l].opacity+=-0.1
            if jeleton[l].opacity<=0.2:
                jeleton[l].opacity=0.2