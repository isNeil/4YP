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

from scipy.spatial.distance import euclidean

from fastdtw import fastdtw



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

def smart_sel2():
    x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
    y = np.array([[2,2], [3,3], [4,4]])
    distance, path = fastdtw(x, y, dist=euclidean)
    print(distance)
        
    
x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
y = np.array([[2,2], [3,3] ,[4,4]])
distance, path = fastdtw(x, y, dist=euclidean)
print(distance)
print(path)
lag=[]
for i in path:
    lag.append(i[0]-i[1])
print(lag)    
############################################################################
#def Dlp(A, B, p=2):
#    cost = np.sum(np.power(np.abs(A - B), p))
#    return np.power(cost, 1 / p)
#
#
#def twed(A, timeSA, B, timeSB, nu, _lambda):
#    # [distance, DP] = TWED( A, timeSA, B, timeSB, lambda, nu )
#    # Compute Time Warp Edit Distance (TWED) for given time series A and B
#    #
#    # A      := Time series A (e.g. [ 10 2 30 4])
#    # timeSA := Time stamp of time series A (e.g. 1:4)
#    # B      := Time series B
#    # timeSB := Time stamp of time series B
#    # lambda := Penalty for deletion operation
#    # nu     := Elasticity parameter - nu >=0 needed for distance measure
#    # Reference :
#    #    Marteau, P.; F. (2009). "Time Warp Edit Distance with Stiffness Adjustment for Time Series Matching".
#    #    IEEE Transactions on Pattern Analysis and Machine Intelligence. 31 (2): 306–318. arXiv:cs/0703033
#    #    http://people.irisa.fr/Pierre-Francois.Marteau/
#
#    # Check if input arguments
#    if len(A) != len(timeSA):
#        print("The length of A is not equal length of timeSA")
#        return None, None
#
#    if len(B) != len(timeSB):
#        print("The length of B is not equal length of timeSB")
#        return None, None
#
#    if nu < 0:
#        print("nu is negative")
#        return None, None
#
#    # Add padding
#    A = np.array([0] + list(A))
#    timeSA = np.array([0] + list(timeSA))
#    B = np.array([0] + list(B))
#    timeSB = np.array([0] + list(timeSB))
#
#    n = len(A)
#    m = len(B)
#    # Dynamical programming
#    DP = np.zeros((n, m))
#
#    # Initialize DP Matrix and set first row and column to infinity
#    DP[0, :] = np.inf
#    DP[:, 0] = np.inf
#    DP[0, 0] = 0
#
#    # Compute minimal cost
#    for i in range(1, n):
#        for j in range(1, m):
#            # Calculate and save cost of various operations
#            C = np.ones((3, 1)) * np.inf
#            # Deletion in A
#            C[0] = (
#                DP[i - 1, j]
#                + Dlp(A[i - 1], A[i])
#                + nu * (timeSA[i] - timeSA[i - 1])
#                + _lambda
#            )
#            # Deletion in B
#            C[1] = (
#                DP[i, j - 1]
#                + Dlp(B[j - 1], B[j])
#                + nu * (timeSB[j] - timeSB[j - 1])
#                + _lambda
#            )
#            # Keep data points in both time series
#            C[2] = (
#                DP[i - 1, j - 1]
#                + Dlp(A[i], B[j])
#                + Dlp(A[i - 1], B[j - 1])
#                + nu * (abs(timeSA[i] - timeSB[j]) + abs(timeSA[i - 1] - timeSB[j - 1]))
#            )
#            # Choose the operation with the minimal cost and update DP Matrix
#            DP[i, j] = np.min(C)
#    distance = DP[n - 1, m - 1]
#    return distance, DP
#def backtracking(DP):
#    # [ best_path ] = BACKTRACKING ( DP )
#    # Compute the most cost efficient path
#    # DP := DP matrix of the TWED function
#
#    x = np.shape(DP)
#    i = x[0] - 1
#    j = x[1] - 1
#
#    # The indices of the paths are save in opposite direction
#    # path = np.ones((i + j, 2 )) * np.inf;
#    best_path = []
#
#    steps = 0
#    while i != 0 or j != 0:
#        best_path.append((i - 1, j - 1))
#
#        C = np.ones((3, 1)) * np.inf
#
#        # Keep data points in both time series
#        C[0] = DP[i - 1, j - 1]
#        # Deletion in A
#        C[1] = DP[i - 1, j]
#        # Deletion in B
#        C[2] = DP[i, j - 1]
#
#        # Find the index for the lowest cost
#        idx = np.argmin(C)
#
#        if idx == 0:
#            # Keep data points in both time series
#            i = i - 1
#            j = j - 1
#        elif idx == 1:
#            # Deletion in A
#            i = i - 1
#            j = j
#        else:
#            # Deletion in B
#            i = i
#            j = j - 1
#        steps = steps + 1
#
#    best_path.append((i - 1, j - 1))
#
#    best_path.reverse()
#    return best_path[1:]
    ######################################################################
    #FDTW
#def FDTW():
#    index=16
#    #not finished want to DTW to either find overall or find path on which to do analysis as above using magnitude difference after warping
#    ref=v1(index)
#    num_plots=len(ref)
#    range_ref=max(ref.iloc[0,:])-min(ref.iloc[0,:])
#    
#    data=v8(index)
#    data_norm1=data.div(range_ref).abs()
#
#    
#    x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
#    y = np.array([[2,2], [3,3], [4,4]])
#    distance, path = fastdtw(x, y, dist=euclidean)
#    return distance