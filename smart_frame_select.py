# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:58:43 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from colour import Color
import time
from v1f import v1
from v2f import v2
from v3f import v3
from v8f import v8
from v9f import v9
from v10f import v10
from v4f import v4
from v11f import v11

def smart_sel():
    index=16
    
    #normalise df
        
    ref=v1(index)
    num_plots=len(ref)
    range_ref=max(ref.iloc[0,:])-min(ref.iloc[0,:])
    
    data=v8(index)
    data_norm1=data.div(range_ref).abs()
    
    ref=v2(index)
    num_plots=len(ref)
    range_ref=max(ref.iloc[0,:])-min(ref.iloc[0,:])
    
    data=v9(index)
    data_norm2=data.div(range_ref).abs()
    
    ref=v3(index)
    num_plots=len(ref)
    range_ref=max(ref.iloc[0,:])-min(ref.iloc[0,:])
    
    data=v10(index)
    data_norm3=data.div(range_ref).abs()
    
    ref=v4(15)
    num_plots=len(ref)
    range_ref=max(ref.iloc[0,:])-min(ref.iloc[0,:])
    
    data=v11(15)
    data_norm4=data.div(range_ref).abs()
    
    norm_sum=data_norm4+data_norm3+data_norm1+data_norm2
    
    
    df=norm_sum
    
    cut_off=[]
    hl=[]
    for i in range(len(df)):
        cut_off.append(np.std(df.iloc[i,:])+np.mean(df.iloc[i,:]))
        temp=[]
        for j in range(np.size(df,1)):
            
            if df.iloc[i,j]>cut_off[i]:
                temp.append(j)
        hl.append(temp)
            
        
    
#    fig, axs = plt.subplots(7,1,figsize=(20, 10))
#    #plt.plot(df.iloc[0,:],'r')
#    axs[0].plot(df.iloc[1,:],'b')
#    for i in hl[1]:
#        axs[0].axvspan(i, i+1, facecolor='grey', alpha=0.5)
#    
#    axs[1].plot(df.iloc[2,:],'y')
#    for i in hl[2]:
#        axs[1].axvspan(i, i+1, facecolor='grey', alpha=0.5)
#    axs[2].plot(df.iloc[3,:],'orange')
#    for i in hl[3]:
#        axs[2].axvspan(i, i+1, facecolor='grey', alpha=0.5)
#    
#    axs[3].plot(df.iloc[4,:],'purple')
#    for i in hl[4]:
#        axs[3].axvspan(i, i+1, facecolor='grey', alpha=0.5)
#    
#    axs[4].plot(df.iloc[5,:],'green')
#    for i in hl[5]:
#        axs[4].axvspan(i, i+1, facecolor='grey', alpha=0.5)
#    
#    axs[5].plot(df.iloc[6,:],'black')
#    for i in hl[6]:
#        axs[5].axvspan(i, i+1, facecolor='grey', alpha=0.5)
#    
#    axs[6].plot(df.iloc[7,:],'grey')
#    for i in hl[7]:
#        axs[6].axvspan(i, i+1, facecolor='grey', alpha=0.5)
#    
#    fig.tight_layout()

    return hl