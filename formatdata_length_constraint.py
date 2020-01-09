# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:39:38 2020

@author: neilw
"""
import pandas as pd
#import json
import numpy as np
#box()
def format(json_file,bones,joints,limb_length):
    df = pd.read_json(json_file)
    
    for i in range(np.shape(df)[1]): 
        for j in range(np.shape(df)[0]):
            df[i][j]=df[i][j].get("translate")
    
    #centre coordinates on hip
       
    for i in range(np.shape(df)[1]):
        shift=df[i][0]
        for j in range(np.shape(df)[0]):
            df[i][j]=np.subtract(df[i][j],shift)
    
###################################################################
    #limb length constraint
    
    df_new=pd.DataFrame.copy(df)
    
    for frame in range(np.shape(df)[0]):
        for i in range(len(bones)):
            start=df[frame][bones[i][0]]
            end=df[frame][bones[i][1]]
            delta=np.subtract(end,start)
            delta_new=np.divide(delta,np.linalg.norm(delta)/limb_length[i])
            
            #sets end joint of first limb by taking start joint coord and adding 
            #constrained length vector
            if i ==0:
                df_new[frame][bones[i][1]]=np.add(start,delta_new)
            else:
                start=df_new[frame][bones[i][0]]
                df_new[frame][bones[i][1]]=np.add(start,delta_new)
    
    return df
