# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 02:06:36 2020

@author: neilw
"""
plotpositionalderivatives(index,bones,joints,plot_num):
    df=v15()
    def plot(axis,dist3,dist3p,color,color2,space):
        
       
        for i in range(len(dist3)):
            y=[dist3[i],dist3p[i]]
            x=[i+space,i+space]
            y2=[dist3[i],(dist3[i]+dist3p[i])/2]
            axis.plot(x,y, color, alpha=1)
            axis.plot(x,y2, color2, alpha=1)
    
    plot(axs[4,0],df[0],df[1],"r","pink",0)
    plot(axs[4,0],df[2*plot_num],df[2*plot_num+1],"b","aqua",0.5)
    axs[4,0].set_ylabel('Distance')
    axs[4,0].set_xlabel('Frame') 
    
bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
#for i in range(0,8):
#    plotpositionalderivatives(16,bones,joints,i)