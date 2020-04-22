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
top=[3,5,2]
comi=7
refi=2


dtwdlist=dtwrecon(top,v1(3))
euc_diff=[]
for i in range(np.size(dtwdlist,1)):
    rangel=abs(max(dtwdlist[:][i])-min(dtwdlist[:][i]))
    euc_diff.append(abs(dtwdlist.iloc[comi][i]-dtwdlist.iloc[refi][i])/rangel)
plt.figure()
plt.plot(euc_diff,'b') 
#plt.savefig("Images/rfootdist.jpg", dpi=100) 

dtwdlist=dtwrecon(top,v17(7))
euc_diff=[]
for i in range(np.size(dtwdlist,1)):
    rangel=abs(max(dtwdlist[:][i])-min(dtwdlist[:][i]))
    euc_diff.append(abs(dtwdlist.iloc[comi][i]-dtwdlist.iloc[refi][i])/rangel)
plt.figure()
plt.plot(euc_diff,'r') 
