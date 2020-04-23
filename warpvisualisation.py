# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 00:42:50 2020

@author: neilw
"""
import matplotlib.pyplot as plt
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np
from v1f import v1
from dtw_combined2 import smart_sel2


def dtwdnew(data,comi,refi):

    path=smart_sel2(data,refi,comi)
    lag=[]
    for i in path:
        lag.append(i[0]-i[1])
    #print(lag)
    com=[]
    ref=[]
    for i in range(np.size(data,1)):
        com.append(data.iloc[comi][i])
        ref.append(data.iloc[refi][i]) 
    difference=[]
    for i in path:
        difference.append(abs(com[i[0]]-ref[i[1]]))
    
    lag4real=[]
    
    
    for i in range(1,len(path)):
        xprev=path[i-1][1]
        x=path[i][1]
        yprev=path[i-1][0]
        y=path[i][0]
        if x>xprev:
            lag4real.append(yprev)
    
    lag4real.append(y)   
    lag4real2=lag4real.copy()
    for i in range(len(lag4real)-1):
        lag4real2[i]=lag4real[i+1]-lag4real[i]
    lag4real2[-1]=0
        
#    plt.figure(0)
#    plt.plot(lag4real2)
#    plt.ylabel('Relative Rate')
#    plt.xlabel('Frame')
#    plt.grid(True)
    return lag4real2
    #plt.savefig("Images/rateof1_7.jpg", dpi=100) 
    
#
#from dtaidistance import dtw
#from dtaidistance import dtw_visualisation as dtwvis
#
#
#
#s1 = np.array(data.iloc[2])
#s2 = np.array(data.iloc[7])
#path = dtw.warping_path(s1, s2)
#dtwvis.plot_warping(s1, s2, path, filename="warp.png" )
data = v1(13)
dtwdnew(data,2,7)