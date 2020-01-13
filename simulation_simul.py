# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:20:39 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np
import joint_angle as ja
from collections import Counter
import scipy
from colour import Color
#simulates a single frame
def sim(skeleton,jeleton,frame,data_f,bones,joints,limb_length,trace_colour,vis=True,ball=True,col=vec(1,1,1)):


    rate(25)
    
    if frame==0:
        
        for i in range(len(bones)):
            start=data_f[frame][bones[i][0]]
            end=data_f[frame][bones[i][1]]
            delta=np.subtract(end,start)
            
            
            skeleton.append(cylinder(pos=vector(start[0],start[1],start[2]), axis=vector(delta[0],delta[1],delta[2]), radius=20, color=col))
            skeleton[-1].visible= vis
        
        for i in range(len(joints)):
            start=data_f[frame][joints[i]]

            jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30,color=col))
            jeleton[-1].visible= vis
#                if i==len(joints)-1:
#                    jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30, make_trail=True, trail_color=trace_colour))
#                    
#                else:
#                    jeleton.append(sphere(pos=vector(start[0],start[1],start[2]), radius=30))
    ##############################################################################
    #Animation
    else:

        for i in range(len(bones)):
            start=data_f[frame][bones[i][0]]
            end=data_f[frame][bones[i][1]]
            delta=np.subtract(end,start)
#                if i == 15:
 #                   print(np.linalg.norm(delta))
            
            skeleton[i].pos=vector(start[0],start[1],start[2])
            skeleton[i].axis=vector(delta[0],delta[1],delta[2])
            
        for i in range(len(joints)):
            start=data_f[frame][joints[i]]
            jeleton[i].pos=vector(start[0],start[1],start[2])
    
#########################################################################################################################
#attach trail , type points not so good actually
    if ball == True:
        a=attach_trail(jeleton[-1],color=trace_colour,type="points")    
        b=attach_trail(jeleton[-2],color=trace_colour,type="points")
        
    elif ball ==False:
        a=attach_trail(jeleton[-1],color=trace_colour)    
        b=attach_trail(jeleton[-2],color=trace_colour)
    

    return [skeleton,jeleton]
            
#