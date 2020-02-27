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



fig = plt.figure(figsize=(20,10))

df=norm_sum








plt.plot(df.iloc[0,:],'r')
plt.plot(df.iloc[1,:],'b')
plt.plot(df.iloc[2,:],'y')
plt.plot(df.iloc[3,:],'orange')
plt.plot(df.iloc[4,:],'purple')
plt.plot(df.iloc[5,:],'green')
plt.plot(df.iloc[6,:],'black')
plt.plot(df.iloc[7,:],'grey')

axs[0,0].set_ylabel('Distance')
axs[0,0].set_xlabel('Frame')

