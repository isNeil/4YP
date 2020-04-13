# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 03:59:08 2020

@author: neilw
"""
import numpy as np
import pandas as pd

def vel(pos1,pos2):
    v=np.subtract(pos2,pos1)
    return v
    
#speed=np.linalg.norm(v)
    
def accel(v1,v2):
    a = np.subtract(v2,v1)
    return a

    
def df_v(data):
    df_vel=pd.DataFrame.copy(data)
    
    for i in range(np.size(data,0)):
        for f in range(np.size(data,1)):
            if f == 0:
                v = [0,0,0]
                         
            else:
                v=vel(data[f][i],data[f-1][i])

            
            df_vel[f][i]=v

    
    return df_vel

def df_a(df_vel):
    df_accel=pd.DataFrame.copy(df_vel)  
    
    for i in range(np.size(df_vel,0)):
        for f in range(np.size(df_vel,1)):
            if f == 0 or f==1:
                a = [0,0,0]
                         
            else:
                
                a=accel(df_vel[f][i],df_vel[f-1][i])
            
            df_accel[f][i]=a

    return df_accel            