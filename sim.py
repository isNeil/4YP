# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:20:00 2020

@author: neilw
"""

from vpython import *
import numpy as np
from colour import Color

#simulates any frame after objects initialised
def create_frame(skeleton,jeleton,frame,data_f,bones,joints,vis=True,tra=True):

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
       

##attach trail , type points not so good actually
#    if tra == True:
#        a=attach_trail(jeleton[-1],color=trace_colour)    
#        b=attach_trail(jeleton[-2],color=trace_colour)
#        


    return [skeleton,jeleton]
            
#