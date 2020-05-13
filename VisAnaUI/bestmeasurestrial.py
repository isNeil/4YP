# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:50:59 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colour import Color
from extractframes import extractframes
from matplotlib.patches import ConnectionPatch
from v1f import v1
from v2f import v2
from v3f import v3
from v5f import v5
from v6f import v6
from v8f import v8
from v9f import v9
from v10f import v10
from v4f import v4
from v11f import v11
from v15f import v15
from v16f import v16
from v17f import v17
from v18f import v18
from dtw_combined2 import dtwd
from dtw_combined2 import dtwrecon
from dtw_combined2 import smart_sel2
from warpvisualisation import dtwdnew
import pickle
import matplotlib
from matplotlib import cm

def plotpositionalderivatives(plot_num):
    
    #plot number starts from 0 i.e. plot 0  is for rf3
    top=[3,5,2]
  
    # Y coordinate of the spine keypoint, Z coordinate of the spine keypoint,
    #Xcoordinate of the right wrist keypoint, Z coordinate of the right foot keypoint 
    #and angle at the left kneekeypoint
    # VAR=distance of right foot, distance of right elbow, angle at the right knee
    # X coordinate of the left foot and Z coordinate of the left arm
    
    
    fig, axs = plt.subplots(4,2,figsize=(22,10))
    fig.subplots_adjust(left=0.03, bottom=0.06, right=0.99, top=0.96, wspace=0.08, hspace=0.34)

    axs[0,0].title.set_text('Spine ')
    axs[1,0].title.set_text('Spine ')
    axs[2,0].title.set_text('R Wrist ')
    axs[3,0].title.set_text('R Foot')
    axs[0,1].title.set_text('R Foot')
    axs[1,1].title.set_text('R Elbow')
    axs[2,1].title.set_text('R Knee')
    axs[3,1].title.set_text('L Foot')
    
    hl= extractframes(v17(7),plot_num)
    for i in hl:
        axs[0,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
 
    hl= extractframes(v18(7),plot_num)
    for i in hl:
        axs[1,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
    
    hl= extractframes(v16(16),plot_num)
    for i in hl:
        axs[2,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
    
    hl= extractframes(v18(3),plot_num)
    for i in hl:
        axs[3,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
    
    hl= extractframes(v1(3),plot_num)
    for i in hl:
        axs[0,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
    
    hl= extractframes(v1(15),plot_num)
    for i in hl:    
        axs[1,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
    
    hl= extractframes(v4(2),plot_num)
    for i in hl:
        axs[2,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
    
    hl= extractframes(v16(6),plot_num)
    for i in hl:
        axs[3,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        
              
    df=dtwrecon(top,v17(7))
    axs[0,0].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[0,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[2,:],'r')
    axs[0,0].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[0,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[7,:],'g',alpha=0.3) 
    axs[0,0].plot(df.iloc[plot_num,:],'black')
    axs[0,0].set_ylabel('Displacement Y')
   # axs[0,0].set_xlabel('Frame')   

    df=dtwrecon(top,v18(7))
    axs[1,0].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[1,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[1,0].plot(df.iloc[2,:],'r')
    axs[1,0].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[1,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[1,0].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[1,0].plot(df.iloc[7,:],'g',alpha=0.3) 
    axs[1,0].plot(df.iloc[plot_num,:],'black')
    axs[1,0].set_ylabel('Displacement Z')
   # axs[0,0].set_xlabel('Frame')   



    
    df2=dtwrecon(top,v16(16))
    axs[2,0].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[2,0].plot(df.iloc[2,:],'r')
    axs[2,0].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[2,0].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[0,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[2,0].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[plot_num,:],'black')
    axs[2,0].set_ylabel('Displacement X')
  #  axs[2,0].set_xlabel('Frame')

    df3=dtwrecon(top,v18(3))
    axs[3,0].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[3,0].plot(df.iloc[2,:],'r')
    axs[3,0].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[3,0].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[0,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[3,0].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[plot_num,:],'black')
    axs[3,0].set_ylabel('Displacement Z')
    axs[3,0].set_xlabel('Frame')


  
  
    df=dtwrecon(top,v1(3))
    axs[0,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[2,:],'r')
    axs[0,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[plot_num,:],'black')
    axs[0,1].set_ylabel('Distance')
 #   axs[0,1].set_xlabel('Frame')    
    #normalise
  
        
    df=dtwrecon(top,v1(15))
    axs[1,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[2,:],'r')
    axs[1,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[2,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[1,1].plot(df.iloc[plot_num,:],'black')
    axs[1,1].set_ylabel('Distance')
  #  axs[1,1].set_xlabel('Frame')
    #normalise


    df=dtwrecon(top,v4(2))
    axs[2,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[2,:],'r')
    axs[2,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[2,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[2,1].plot(df.iloc[plot_num,:],'black')
    axs[2,1].set_ylabel('Angle')
   # axs[2,1].set_xlabel('Frame')   

 
    df=dtwrecon(top,v16(6))
    axs[3,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[2,:],'r')
    axs[3,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[3,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[3,1].plot(df.iloc[plot_num,:],'black')
    axs[3,1].set_ylabel('Displacement X')
    axs[3,1].set_xlabel('Frame')
    #normalise



#    fig.tight_layout()

#    for preload
    plt.savefig("Images/UIresize2/bestmeasures_%d.jpg"%(plot_num), dpi=96)  




#    for preload
#    plt.savefig("Images/UIresize2/stdvis_trial_%d_keypoint_%d.jpg"%(plot_num,index), dpi=96)  


#    plt.subplot_tool()
#    plt.show()


#bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
#joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
#
for i in range(2,10): 

    
    plotpositionalderivatives(i)
    plt.close()


#plotpositionalderivatives2(4,bones,joints,1)
