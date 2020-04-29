# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 05:26:23 2020

@author: neilw
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from v17f import v17
from v4f import v4
from v1f import v1
from v6f import v6

def smart_sel2(data,refi,comi):
    #no normalisation as I'm only analysing with position to begin with     
    #hardcoding analyse foot
    #refi is index of best trial
    #
    
    com=[]
    ref=[]

    for i in range(np.size(data,1)):
        com.append([i,data.iloc[comi][i]])
        ref.append([i,data.iloc[refi][i]])      
    x = np.asarray(com, dtype=np.float32)
    y = np.asarray(ref, dtype=np.float32)
    distance, path = fastdtw(x, y, dist=euclidean)
    
   # print(distance)

    return path



def dtwd(data,refi,comi):

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
    
    

    dtwd=[]
    
    for i in range(len(data.iloc[refi])):
        x=i+lag[i]
        if x<len(data.iloc[refi]):
            dtwd.append(data.iloc[comi][x])
        else:
            dtwd.append(dtwd[-1]) #to use previous point since no more data
    return dtwd




def dtwrecon(top,vdata):
    #vdata is which v#f(index) you choose
    
    #top are the plots you want to cluster, top and bott should be in descending performance
    #top=[3,5,2]
    #bott=[1,10,8,9,4,6]
    
    data=vdata.copy()
    refi=top[0]-1
    
    dtwdlist=data.copy()
    
    
    for i in range(len(data)):
        dtwed=dtwd(data,refi,i)
        for j in range(np.size(data,1)):
            dtwdlist.iloc[i][j]=dtwed[j]
        
        
        if i != 6:
            if i ==2:
                
                plt.plot(dtwdlist.iloc[i],'blue',alpha=1)
            if i == 1:
                plt.plot(dtwdlist.iloc[i],'blue',alpha=0.8)
            if i == 4:
                plt.plot(dtwdlist.iloc[i],'blue',alpha=0.8)
            else:
                plt.plot(dtwdlist.iloc[i],'green',alpha=0.4)
        
        
         
        
    plt.ylabel('Distance')
    plt.xlabel('Frame')
    plt.grid(True)
    plt.xlim((0,140))
#    
    return dtwdlist


def dtwhighlight(top,bott,dtwdlist):  
    #returns allstats which contains differences for variance and mean
    #colours in for top 80% of input measure
    #avoid small ranges which don't tell much in mm 
    min_rang=3
    
    frame_good=[]
    frame_bad=[]
    differences_mean=[]
    differences_var=[]
    allstats=[]
    norm_dtwdlist=dtwdlist.copy()
    
    for i in range(np.size(dtwdlist,1)): 
        minval=min(dtwdlist.iloc[:][i])
       
        rang=max(dtwdlist.iloc[:][i])-minval
        
        if rang<min_rang:
            allstats.append([0])
            differences_mean.append(0)
            differences_var.append(0)
        else:
            for j in range(len(dtwdlist)):
                norm_dtwdlist.iloc[j][i]=(dtwdlist.iloc[j][i]-minval)/rang
            
            
            for j in top:
                frame_good.append(norm_dtwdlist.iloc[j-1][i])
            mean_good=np.mean(frame_good)
            var_good=np.var(frame_good)
            
            
            for k in bott:    
                
                frame_bad.append(norm_dtwdlist.iloc[k-1][i])
            mean_bad= np.mean(frame_bad)
            var_bad=np.var(frame_bad)
                    

            allstats.append([var_bad,var_good,mean_bad,mean_good])
            differences_mean.append(abs(mean_bad-mean_good))
            differences_var.append(abs(var_bad-var_good))


        frame_good=[]
        frame_bad=[]


     #ascending order
    differences_mean_sorted=sorted(differences_mean)
    differences_var_sorted=sorted(differences_var)
    
    cutoff_mean=differences_mean_sorted[int(np.floor(len(differences_mean)*0.8))]
    cutoff_var=differences_var_sorted[int(np.floor(len(differences_var)*0.8))]

    chose_times_mean=[]
    chose_times_var=[]
    for i in range(len(differences_mean)):
        if differences_mean[i] > cutoff_mean:
            chose_times_mean.append(i)
        if differences_var[i] > cutoff_var:    
            chose_times_var.append(i)
    
#    for i in chose_times_mean:
#        plt.axvspan(i, i+1, facecolor='grey', alpha=0.3)
#    for i in chose_times_var:
#        plt.axvspan(i, i+1, facecolor='red', alpha=0.3)

    
    return [chose_times_mean,chose_times_var,allstats,differences_mean,differences_var]




#
top=[3,5,2]
bott=[1,10,8,9,4,6]
dtwdlist=dtwrecon(top,v17(7))
##plt.savefig("Images/rfootdist.jpg", dpi=100) 
#[chose_times_mean,chose_times_var,allstats,differences_mean,differences_var]=dtwhighlight(top,bott,dtwdlist)

