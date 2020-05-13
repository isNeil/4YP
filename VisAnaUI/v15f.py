"""
Created on Sat Mar 28 03:28:46 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon
from mpl_toolkits.mplot3d import Axes3D
from colour import Color
import time
from operator import add
from matplotlib.collections import PatchCollection


def v15(index):
    plot3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\3.json')
    plot4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\4.json')
    plot5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\5.json')
    plot6= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\6.json')
    plot7= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\7.json')
    plot8= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\8.json')
    plot9= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\9.json')
    plot10= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\10.json')
    
    
    #    #index mapping
    #    bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
        
    #joint 0 to 27 Rwrist
    dist1=[]
    dist1p=[]
    dist2=[]
    dist2p=[]       
    dist3=[]
    dist3p=[]
    dist4=[]
    dist4p=[]
    dist5=[]
    dist5p=[]
    dist6=[]
    dist6p=[]
    dist7=[]
    dist7p=[]
    dist8=[]
    dist8p=[]
    dist9=[]
    dist9p=[]
    dist10=[]
    dist10p=[]
       
    
    #mapping index to joint 
    dex=joints[index]
    
    
    #for i in range(np.shape(plot1)[1]):
    #    dist.append(((plot1.iloc[dex][i][0])**2+(plot1.iloc[dex][i][1])**2+(plot1.iloc[dex][i][2])**2)**0.5)
    for i in range(np.shape(plot3)[1]):
        dist1.append(((plot3.iloc[dex][i][0])**2+(plot3.iloc[dex][i][1])**2+(plot3.iloc[dex][i][2])**2)**0.5)    
        dist1p.append(((plot3.iloc[dex-1][i][0])**2+(plot3.iloc[dex-1][i][1])**2+(plot3.iloc[dex-1][i][2])**2)**0.5)  
        dist2.append(((plot3.iloc[dex][i][0])**2+(plot3.iloc[dex][i][1])**2+(plot3.iloc[dex][i][2])**2)**0.5)    
        dist2p.append(((plot3.iloc[dex-1][i][0])**2+(plot3.iloc[dex-1][i][1])**2+(plot3.iloc[dex-1][i][2])**2)**0.5)  
        dist3.append(((plot3.iloc[dex][i][0])**2+(plot3.iloc[dex][i][1])**2+(plot3.iloc[dex][i][2])**2)**0.5)    
        dist3p.append(((plot3.iloc[dex-1][i][0])**2+(plot3.iloc[dex-1][i][1])**2+(plot3.iloc[dex-1][i][2])**2)**0.5)     
        dist4.append(((plot4.iloc[dex][i][0])**2+(plot4.iloc[dex][i][1])**2+(plot4.iloc[dex][i][2])**2)**0.5)   
        dist4p.append(((plot4.iloc[dex-1][i][0])**2+(plot4.iloc[dex-1][i][1])**2+(plot4.iloc[dex-1][i][2])**2)**0.5)
        dist5.append(((plot5.iloc[dex][i][0])**2+(plot5.iloc[dex][i][1])**2+(plot5.iloc[dex][i][2])**2)**0.5)
        dist5p.append(((plot5.iloc[dex-1][i][0])**2+(plot5.iloc[dex-1][i][1])**2+(plot5.iloc[dex-1][i][2])**2)**0.5)
        dist6.append(((plot6.iloc[dex][i][0])**2+(plot6.iloc[dex][i][1])**2+(plot6.iloc[dex][i][2])**2)**0.5) 
        dist6p.append(((plot6.iloc[dex-1][i][0])**2+(plot6.iloc[dex-1][i][1])**2+(plot6.iloc[dex-1][i][2])**2)**0.5)
        dist7.append(((plot7.iloc[dex][i][0])**2+(plot7.iloc[dex][i][1])**2+(plot7.iloc[dex][i][2])**2)**0.5)
        dist7p.append(((plot7.iloc[dex-1][i][0])**2+(plot7.iloc[dex-1][i][1])**2+(plot7.iloc[dex-1][i][2])**2)**0.5)  
        dist8.append(((plot8.iloc[dex][i][0])**2+(plot8.iloc[dex][i][1])**2+(plot8.iloc[dex][i][2])**2)**0.5)
        dist8p.append(((plot8.iloc[dex-1][i][0])**2+(plot8.iloc[dex-1][i][1])**2+(plot8.iloc[dex-1][i][2])**2)**0.5)
        dist9.append(((plot9.iloc[dex][i][0])**2+(plot9.iloc[dex][i][1])**2+(plot9.iloc[dex][i][2])**2)**0.5)
        dist9p.append(((plot9.iloc[dex-1][i][0])**2+(plot9.iloc[dex-1][i][1])**2+(plot9.iloc[dex-1][i][2])**2)**0.5)
        dist10.append(((plot10.iloc[dex][i][0])**2+(plot10.iloc[dex][i][1])**2+(plot10.iloc[dex][i][2])**2)**0.5)
        dist10p.append(((plot10.iloc[dex-1][i][0])**2+(plot10.iloc[dex-1][i][1])**2+(plot10.iloc[dex-1][i][2])**2)**0.5)
    
     
    ######################################Below this should be a function but for now just do x
    
    
#    
#    fig, ax = plt.subplots(figsize=(10, 3))
#    #fig = plt.figure(figsize=(10, 3))
#
#    
#    plt.fill_between(range(102),dist3,dist3p,alpha=0.2,color="blue")
#    plt.plot(dist3,color="blue",alpha=0.6)
#    plt.fill_between(range(102),dist4,dist4p,alpha=0.2,color="red")
#    plt.plot(dist4,color="red",alpha=0.6)  
#    plt.fill_between(range(102),dist6,dist6p,alpha=0.2,color="green")   
#    plt.plot(dist6,color="green",alpha=0.6)
#    plt.fill_between(range(102),dist5,dist5p,alpha=0.2,color="yellow") 
#    plt.plot(dist5,color="yellow",alpha=0.6)
#    
#    
#
#    
#    
#    
#    plt.ylabel('Distance')
#    plt.xlabel('Frame')
#    plt.grid(True)
#    
#    plt.xlim((0,102))
#    plt.ylim((200,1000))
#    #ax.add_collection(p1)
#    
#    
#    
#     
#    
#    plt.show()
#    

    df = pd.DataFrame(np.array([dist1,dist2,dist3,dist4,dist5,dist6,dist7,dist8,dist9,dist10]))

    return df

#v15(16)
    
    
        
        
        
