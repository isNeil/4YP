# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:20:39 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np
from formatdata import format
from collections import Counter
import scipy

def sim(frame,data_f,bones,joints,limb_length,trace_colour):
    data_f_new=pd.DataFrame.copy(data_f)
    skeleton=[]
    jeleton=[]
#    length=[]
    
    for i in range(len(bones)):
        start=data_f[frame][bones[i][0]]
        end=data_f[frame][bones[i][1]]
        delta=np.subtract(end,start)
        delta_n=np.divide(delta,np.linalg.norm(delta)/limb_length[i])
        
#        length.append(np.linalg.norm(delta))
        
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
        start=data_f_new[frame][joints[i]]
        if i==len(joints)-1:
            jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30,make_trail=True, trail_color=trace_colour))
            
        else:
            jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30))
    ##############################################################################
    ##############################################################################
    #Animation start
    
    while frame<np.shape(data_f)[1]-1:
    
        rate(25)
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
    ##################################################################################
  # plot trails 
        k=20
        k_skeleton=[]
  
        if frame%k==0:
            for i in range(len(bones)):
                
                start=data_f[frame][bones[i][0]]
                end=data_f[frame][bones[i][1]]
                delta=np.subtract(end,start)
                delta_n=np.divide(delta,np.linalg.norm(delta)/limb_length[i])
        
#                length.append(np.linalg.norm(delta))
        
                if i ==0:
                    skeleton.append(cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta_n[0],delta_n[1],delta_n[2]), radius=20, opacity=1))
                    data_f_new[frame][bones[i][1]]=np.add(start,delta_n)
                else:

                    start=data_f_new[frame][bones[i][0]]
                    skeleton.append(cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta_n[0],delta_n[1],delta_n[2]), radius=20, opacity=1))

    #        if i in joints:
    #            jeleton.append(sphere(pos=vector(endpoint[0],endpoint[1],endpoint[2]), radius=30))
                    data_f_new[frame][bones[i][1]]=np.add(start,delta_n)
     
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
#########################################################################################################################
        
                
    return data_f_new
            