# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:27:24 2020

@author: neilw
"""
import numpy as np
from dtw_combined2 import dtwd
from dtw_combined2 import dtwrecon
import matplotlib.pyplot as plt
from v1f import v1
from v17f import v17
from v18f import v18
from v4f import v4
from v16f import v16



def extractframes(bestmeasure,comi):
    refi=2
    refi2=1
    refi3=4        
    top=[3,5,2]
    dtwdlist=dtwrecon(top,bestmeasure)
    euc_diff=[]
    for i in range(np.size(dtwdlist,1)):
        rangel=abs(max(dtwdlist[:][i])-min(dtwdlist[:][i]))
        rangemax=max(dtwdlist.iloc[refi][i],dtwdlist.iloc[refi2][i],dtwdlist.iloc[refi3][i])
        rangemin=min(dtwdlist.iloc[refi][i],dtwdlist.iloc[refi2][i],dtwdlist.iloc[refi3][i])
        if dtwdlist.iloc[comi][i]>rangemax:
            euc_diff.append(abs(dtwdlist.iloc[comi][i]-rangemax)/rangel)
        
        elif dtwdlist.iloc[comi][i]<rangemin:
            euc_diff.append(abs(rangemin-dtwdlist.iloc[comi][i])/rangel)
        else:
            euc_diff.append(0)
            
    
    #
    
    euc_sort=sorted(euc_diff)
    
    x=euc_sort[int(np.floor(0.8*len(euc_sort)))]
    
    choose=[]
    for i in range(len(euc_diff)):
        if euc_diff[i] > x:
            choose.append(i)
            
    return choose

#bestmeasure=v1(3)
#top=[3,5,2]
#comi=7
#refi=2
#choose=extractframes(bestmeasure,comi)
#
#dtwdlist=dtwrecon(top,bestmeasure)
#
#plt.figure()
#plt.plot(dtwdlist.iloc[refi][:],'r')
#plt.plot(dtwdlist.iloc[comi][:],'g')
#
#
#plt.ylabel('Distance')
#plt.xlabel('Frame')
#plt.grid(True)
#plt.xlim((0,140))
#for i in choose:
#    plt.axvspan(i, i+1, facecolor='grey', alpha=0.3)
#plt.savefig("Images/comparhighlighted.jpg", dpi=100) 