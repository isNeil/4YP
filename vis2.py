# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:22:35 2020

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

def plotpositionalderivatives(index,bones,joints,plot_num):
    
    #plot number starts from 0 i.e. plot 0  is for rf3
    top=[3,5,2]
  
    hl= extractframes(v1(3),plot_num)
    
    
    fig, axs = plt.subplots(4,2,figsize=(22,10))
    fig.subplots_adjust(left=0.03, bottom=0.06, right=0.99, top=0.96, wspace=0.08, hspace=0.34)

    axs[0,0].title.set_text('No DTW')
    axs[1,0].title.set_text('Relative Rate of comparison w.r.t. reference')
    axs[2,0].title.set_text('DTW w.r.t. comparison.')
    axs[3,0].title.set_text('DTW w.r.t. reference')
    axs[0,1].title.set_text('DTW w.r.t reference')
    axs[1,1].title.set_text('DTW w.r.t reference')
    axs[2,1].title.set_text('DTW w.r.t reference')
    axs[3,1].title.set_text('DTW w.r.t reference')
    
    for i in hl:
#        axs[0,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
#        axs[1,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
#        axs[2,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[3,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)

        axs[0,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[1,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[2,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[3,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        
    path=smart_sel2(v1(index),top[0]-1,plot_num)
    new_hl=[]
    for i in path:
        if i[1] in hl:
              new_hl.append(i[0])  
    for i in new_hl:
        axs[2,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
                 
              
    df=v1(index)
    axs[0,0].plot(df.iloc[0,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[2,:],'r')
    axs[0,0].plot(df.iloc[3,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[5,:],'b',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[7,:],'b',alpha=0.3) 
    axs[0,0].plot(df.iloc[plot_num,:],'black')
    axs[0,0].set_ylabel('Distance')
   # axs[0,0].set_xlabel('Frame')   



    dfata=dtwdnew(v1(index),2,plot_num)

    axs[1,0].plot(dfata)
#    for i in range(len(dfata)):
#        if dfata[i]>1:
#            axs[2,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
#        elif dfata[i]<1:
#            axs[2,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
#            
#    
    
    axs[1,0].set_ylabel('Relative Rate')
  #  axs[1,0].set_xlabel('Frame')   
    
        
#    dfata=dtwdnew(v1(index),plot_num,2)
#    for i in range(len(dfata)):
#        if dfata[i]>1:
#            axs[3,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
#        elif dfata[i]<1:
#            axs[3,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
#    dfataref=np.zeros(len(path))
#    for i in path:
#        dfataref[i[0]]=dfata[i[1]]
#    for i in range(len(dfataref)):
#        if dfataref[i]>1:
#            axs[3,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
#        elif dfataref[i]<1:
#            axs[3,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
    
    df2=dtwrecon([plot_num+1],v1(index))
    axs[2,0].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[2,0].plot(df.iloc[2,:],'r')
    axs[2,0].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[2,0].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[0,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[2,0].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[plot_num,:],'black')
    axs[2,0].set_ylabel('Distance')
  #  axs[2,0].set_xlabel('Frame')

    df3=dtwrecon(top,v1(index))
    axs[3,0].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[3,0].plot(df.iloc[2,:],'r')
    axs[3,0].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[3,0].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[0,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[3,0].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[plot_num,:],'black')
    axs[3,0].set_ylabel('Distance')
    axs[3,0].set_xlabel('Frame')

    
##########################################################################
#
    for i in range(len(path)):
        if dfata[path[i][1]]!=1:
            xycom = (path[i][1],df2.iloc[plot_num,path[i][1]])
            xyref = (path[i][0],df3.iloc[2,path[i][0]])
            
            con = ConnectionPatch(xyA=xycom, xyB=xyref, coordsA="data", coordsB="data", axesA=axs[2,0], axesB=axs[3,0], color="orange",shrinkA=0.0, shrinkB=0.0)
        
            axs[3,0].add_artist(con)
        if dfata[path[i][1]]>1:     
            xycom = (path[i+1][1],df2.iloc[plot_num,path[i+1][1]])
            xyref = (path[i+1][0],df3.iloc[2,path[i+1][0]])
            con = ConnectionPatch(xyA=xycom, xyB=xyref, coordsA="data", coordsB="data", axesA=axs[2,0], axesB=axs[3,0], color="orange",shrinkA=0.0, shrinkB=0.0)
        
            axs[3,0].add_artist(con)


  ##########################################################################  
    df=dtwrecon(top,v16(index))
    axs[0,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[2,:],'r')
    axs[0,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[plot_num,:],'black')
    axs[0,1].set_ylabel('Displacement X')
 #   axs[0,1].set_xlabel('Frame')    
    #normalise
  
        
    df=dtwrecon(top,v17(index))
    axs[1,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[2,:],'r')
    axs[1,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[2,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[1,1].plot(df.iloc[plot_num,:],'black')
    axs[1,1].set_ylabel('Displacement Y')
  #  axs[1,1].set_xlabel('Frame')
    #normalise


    df=dtwrecon(top,v18(index))
    axs[2,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[2,:],'r')
    axs[2,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[2,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[2,1].plot(df.iloc[plot_num,:],'black')
    axs[2,1].set_ylabel('Displacement Z')
   # axs[2,1].set_xlabel('Frame')   

 
    df=dtwrecon(top,v4(index))
    axs[3,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[2,:],'r')
    axs[3,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[3,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[3,1].plot(df.iloc[plot_num,:],'black')
    axs[3,1].set_ylabel('Angle')
    axs[3,1].set_xlabel('Frame')
    #normalise



    fig.tight_layout()

#    for preload
    plt.savefig("Images/UIresize2/stdvis_trial_%d_keypoint_%d.jpg"%(plot_num,index), dpi=96)  

def plotpositionalderivatives2(index,bones,joints,plot_num):
    #plots for keypoints 1 4 7
    #plot number starts from 0 i.e. plot 0  is for rf3
    top=[3,5,2]
  
    hl= extractframes(v1(3),plot_num)
    
    
    fig, axs = plt.subplots(4,2,figsize=(22,10))
    fig.subplots_adjust(left=0.03, bottom=0.06, right=0.99, top=0.96, wspace=0.08, hspace=0.34)
    axs[0,0].title.set_text('No DTW')
    axs[1,0].title.set_text('Relative Rate of comparison w.r.t. reference')
    axs[2,0].title.set_text('DTW w.r.t. comparison.')
    axs[3,0].title.set_text('DTW w.r.t. reference')
    axs[0,1].title.set_text('DTW w.r.t reference')
    axs[1,1].title.set_text('DTW w.r.t reference')
    axs[2,1].title.set_text('DTW w.r.t reference')
    axs[3,1].title.set_text('DTW w.r.t reference')
    
    for i in hl:
#        axs[0,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
#        axs[1,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
#        axs[2,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[3,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[0,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[1,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[2,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[3,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        
    path=smart_sel2(v4(index),top[0]-1,plot_num)
    new_hl=[]
    for i in path:
        if i[1] in hl:
              new_hl.append(i[0])  
    for i in new_hl:
        axs[2,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
                 
              
    df=v4(index)
    axs[0,0].plot(df.iloc[0,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[2,:],'r')
    axs[0,0].plot(df.iloc[3,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[5,:],'b',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[7,:],'b',alpha=0.3) 
    axs[0,0].plot(df.iloc[plot_num,:],'black')
    axs[0,0].set_ylabel('Angle')
   # axs[0,0].set_xlabel('Frame')   



    dfata=dtwdnew(v4(index),2,plot_num)
#    axs[1,0].bar(range(len(dfata)),dfata)
    axs[1,0].plot(dfata)
#    for i in range(len(dfata)):
#        if dfata[i]>1:
#            axs[2,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
#        elif dfata[i]<1:
#            axs[2,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
            
    
    
    axs[1,0].set_ylabel('Relative Rate')
  #  axs[1,0].set_xlabel('Frame')   
    
        
#    dfata2=dtwdnew(v4(index),plot_num,2)
#    for i in range(len(dfata)):
#        if dfata[i]>1:
#            axs[3,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
#        elif dfata[i]<1:
#            axs[3,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
#    dfataref=np.zeros(len(path))
#    for i in path:
#        dfataref[i[0]]=dfata[i[1]]
#    for i in range(len(dfataref)):
#        if dfataref[i]>1:
#            axs[3,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
#        elif dfataref[i]<1:
#            axs[3,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
    
    df2=dtwrecon([plot_num+1],v4(index))
    axs[2,0].plot(df2.iloc[0,:],'g',alpha=0.3)
    axs[2,0].plot(df2.iloc[1,:],'b',alpha=0.3)
    axs[2,0].plot(df2.iloc[2,:],'r')
    axs[2,0].plot(df2.iloc[3,:],'g',alpha=0.3)
    axs[2,0].plot(df2.iloc[4,:],'b',alpha=0.3)
    axs[2,0].plot(df2.iloc[5,:],'g',alpha=0.3)
    #axs[0,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[2,0].plot(df2.iloc[7,:],'g',alpha=0.3)
    axs[2,0].plot(df2.iloc[plot_num,:],'black')
    axs[2,0].set_ylabel('Angle')
  #  axs[2,0].set_xlabel('Frame')

    df3=dtwrecon(top,v4(index))
    axs[3,0].plot(df3.iloc[0,:],'g',alpha=0.3)
    axs[3,0].plot(df3.iloc[1,:],'b',alpha=0.3)
    axs[3,0].plot(df3.iloc[2,:],'r')
    axs[3,0].plot(df3.iloc[3,:],'g',alpha=0.3)
    axs[3,0].plot(df3.iloc[4,:],'b',alpha=0.3)
    axs[3,0].plot(df3.iloc[5,:],'g',alpha=0.3)
    #axs[0,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[3,0].plot(df3.iloc[7,:],'g',alpha=0.3)
    axs[3,0].plot(df3.iloc[plot_num,:],'black')
    axs[3,0].set_ylabel('Angle')
    axs[3,0].set_xlabel('Frame')

##########################################################################
#
    for i in range(len(path)):
        if dfata[path[i][1]]!=1:
            xycom = (path[i][1],df2.iloc[plot_num,path[i][1]])
            xyref = (path[i][0],df3.iloc[2,path[i][0]])
            
            con = ConnectionPatch(xyA=xycom, xyB=xyref, coordsA="data", coordsB="data", axesA=axs[2,0], axesB=axs[3,0], color="orange",shrinkA=0.0, shrinkB=0.0)
        
            axs[3,0].add_artist(con)
        if dfata[path[i][1]]>1:     
            xycom = (path[i+1][1],df2.iloc[plot_num,path[i+1][1]])
            xyref = (path[i+1][0],df3.iloc[2,path[i+1][0]])
            con = ConnectionPatch(xyA=xycom, xyB=xyref, coordsA="data", coordsB="data", axesA=axs[2,0], axesB=axs[3,0], color="orange",shrinkA=0.0, shrinkB=0.0)
        
            axs[3,0].add_artist(con)
        



  ##########################################################################  
    df=dtwrecon(top,v16(index))
    axs[0,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[2,:],'r')
    axs[0,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[plot_num,:],'black')
    axs[0,1].set_ylabel('Displacement X')
 #   axs[0,1].set_xlabel('Frame')    
    #normalise
  
        
    df=dtwrecon(top,v17(index))
    axs[1,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[2,:],'r')
    axs[1,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[2,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[1,1].plot(df.iloc[plot_num,:],'black')
    axs[1,1].set_ylabel('Displacement Y')
  #  axs[1,1].set_xlabel('Frame')
    #normalise


    df=dtwrecon(top,v18(index))
    axs[2,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[2,:],'r')
    axs[2,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[2,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[2,1].plot(df.iloc[plot_num,:],'black')
    axs[2,1].set_ylabel('Displacement Z')
   # axs[2,1].set_xlabel('Frame')   

 
    df=dtwrecon(top,v1(index))
    axs[3,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[2,:],'r')
    axs[3,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[3,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[3,1].plot(df.iloc[plot_num,:],'black')
    axs[3,1].set_ylabel('Distance')
    axs[3,1].set_xlabel('Frame')
    #normalise




#    for preload
#    plt.savefig("Images/UIresize2/stdvis_trial_%d_keypoint_%d.jpg"%(plot_num,index), dpi=96)  


#    plt.subplot_tool()
#    plt.show()


bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
for i in range(10): 
    for j in range(1,17):
        if j == 1 or j==4 or j==7:
            plotpositionalderivatives2(j,bones,joints,i)
        else:
            plotpositionalderivatives(j,bones,joints,i)
        plt.close()


#plotpositionalderivatives2(4,bones,joints,1)
