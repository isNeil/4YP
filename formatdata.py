# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:45:43 2020

@author: neilw
"""
import pandas as pd
#import json
import numpy as np
#box()
def format(json_file):
    df = pd.read_json(json_file)
    #g = pd.io.json.json_normalize(d)
    #y = json.loadsd[1][1] the JSON object must be str, bytes or bytearray, not 'dict'
    #d.iteritems
    
    #for key, value in d[1][1]:
    #    temp = [key,value]
    #    dictlist.append(temp)
    
    
    for i in range(np.shape(df)[1]): 
        for j in range(np.shape(df)[0]):
            df[i][j]=df[i][j].get("translate")
    
    #centre coordinates on hip
       
        
    for i in range(np.shape(df)[1]): 
        for j in range(np.shape(df)[0]):
            df[i][j]=np.subtract(df[i][j],df[i][0])
    
    return df
        
        