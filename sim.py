# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:20:00 2020

@author: neilw
"""

from vpython import *
import numpy as np
from colour import Color
import pandas as pd
#simulates any frame after objects initialised
def create_frame(skeleton,jeleton,frame,data_f,bones,joints,vis=True):

    for i in range(len(bones)):
        start=data_f[frame][bones[i][0]]
        end=data_f[frame][bones[i][1]]
        delta=np.subtract(end,start)
    
        skeleton[i].pos=vector(start[0],start[1],start[2])
        skeleton[i].axis=vector(delta[0],delta[1],delta[2])
        skeleton[i].visible= vis
        
        
    for i in range(len(joints)):
        start=data_f[frame][joints[i]]
        jeleton[i].pos=vector(start[0],start[1],start[2])
        jeleton[i].visible= vis
       

#attach trail , type points not so good actually
#    if tra == True:
#        a=attach_trail(jeleton[-1])    
#        b=attach_trail(jeleton[-2])
        


    return [skeleton,jeleton]
            
#initialises skeleton in frame position
def frame_init(skeleton,jeleton,frame,data_f,bones,joints,vis=True,col=vec(1,1,1)):
        
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


        

    return [skeleton,jeleton]


def trace_init(trace,data_f,joints, joint_num,vis=False):
    #indexed already so just 1,2,3 .... for a particular joint returns trace
    red = Color("blue")
    colors = list(red.range_to(Color("green"),np.size(data_f,1)))
    #
    
    
    for j in range(np.size(data_f,1)):
        
        rgbc=colors[j].rgb
        start=data_f[j][joints[joint_num]]   
        trace.append(sphere(pos=vector(start[0],start[1],start[2]), radius=5,color=vector(rgbc[0],rgbc[1],rgbc[2])))
         
         
        trace[-1].visible= vis
    return trace

#def trace_move(trace,data_f,joints, joint_num,vis=False):
#    
#    for j in range(np.size(data_f,1)):
#         start=data_f[j][joints[joint_num]] 
#         trace[i].pos=vector(start[0],start[1],start[2]) 
#         trace[i].visible= vis     
#    return trace
    
########################
#bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
#joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]    
#all_traces=[]
#tracetemp=[]
#plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\1.json')
#for j in range(len(joints)):
##    
#    tracejoint = trace_init(tracetemp,plot1,joints,j)
#    all_traces.append(tracejoint)
#    tracetemp=[]
##for i in 
#all_traces[2][100].visible=True
#    i.visible=True
