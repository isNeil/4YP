# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:20:39 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np

from collections import Counter
import scipy
#simulates a single frame
def sim(frame,data_f,bones,joints,limb_length,trace_colour):
    skeleton=[]
    jeleton=[]

    while frame<np.shape(data_f)[1]-1:
    
        rate(25)
        
        if frame==0:
            for i in range(len(bones)):
                start=data_f[frame][bones[i][0]]
                end=data_f[frame][bones[i][1]]
                delta=np.subtract(end,start)
                
                skeleton.append(cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta[0],delta[1],delta[2]), radius=20))
            
            for i in range(len(joints)):
                start=data_f[frame][joints[i]]
                if i==len(joints)-1:
                    jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30,make_trail=True, trail_color=trace_colour))
                    
                else:
                    jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30))
        ##############################################################################
        ##############################################################################
        #Animation start
        else:
    
            
            
            for i in range(len(bones)):
                start=data_f[frame][bones[i][0]]
                end=data_f[frame][bones[i][1]]
                delta=np.subtract(end,start)        
                
                skeleton[i].pos=vector(start[0],start[1],start[2])
                skeleton[i].axis=vector(delta[0],delta[1],delta[2])
                
            for i in range(len(joints)):
                start=data_f[frame][joints[i]]
                jeleton[i].pos=vector(start[0],start[1],start[2])
        frame+=1
    #########################################################################################################################
            
                
    return
            