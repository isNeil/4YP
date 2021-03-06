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


def v1(index):
    plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\1.json')
    plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\2.json')
    plot3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\3.json')
    plot4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\4.json')
    plot5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\5.json')
    plot6= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\6.json')
    plot7= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\7.json')
    plot8= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\8.json')
    plot9= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\9.json')
    plot10= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\10.json')
    
    
    #    #index mapping
#    bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
        
#    index=16
     
    #joint 0 to 27 Rwrist
    dist1=[]
    dist2=[]
    dist3=[]
    dist4=[]
    dist5=[]
    dist6=[]
    dist7=[]
    dist8=[]
    dist9=[]
    dist10=[]
    


    dex=joints[index]
    

    for i in range(np.shape(plot1)[1]):
        dist1.append(((plot1.iloc[dex][i][0])**2+(plot1.iloc[dex][i][1])**2+(plot1.iloc[dex][i][2])**2)**0.5)    
    
        dist2.append(((plot2.iloc[dex][i][0])**2+(plot2.iloc[dex][i][1])**2+(plot2.iloc[dex][i][2])**2)**0.5)    
  
        dist3.append(((plot3.iloc[dex][i][0])**2+(plot3.iloc[dex][i][1])**2+(plot3.iloc[dex][i][2])**2)**0.5)    
        
        dist4.append(((plot4.iloc[dex][i][0])**2+(plot4.iloc[dex][i][1])**2+(plot4.iloc[dex][i][2])**2)**0.5)
   
        dist5.append(((plot5.iloc[dex][i][0])**2+(plot5.iloc[dex][i][1])**2+(plot5.iloc[dex][i][2])**2)**0.5)
       
        dist6.append(((plot6.iloc[dex][i][0])**2+(plot6.iloc[dex][i][1])**2+(plot6.iloc[dex][i][2])**2)**0.5)
    
        dist7.append(((plot7.iloc[dex][i][0])**2+(plot7.iloc[dex][i][1])**2+(plot7.iloc[dex][i][2])**2)**0.5)
    
        dist9.append(((plot9.iloc[dex][i][0])**2+(plot9.iloc[dex][i][1])**2+(plot9.iloc[dex][i][2])**2)**0.5)
  
        dist10.append(((plot10.iloc[dex][i][0])**2+(plot10.iloc[dex][i][1])**2+(plot10.iloc[dex][i][2])**2)**0.5)
      
        dist8.append(((plot8.iloc[dex][i][0])**2+(plot8.iloc[dex][i][1])**2+(plot8.iloc[dex][i][2])**2)**0.5)
        
    #######################################Below this should be a function but for now just do x
    
    

    fig = plt.figure(figsize=(10, 3))

    plt.plot(dist1,"b",alpha=0.4)
    plt.plot(dist2,"yellow",alpha=1)
    plt.plot(dist3,"red",alpha=1) 
    plt.plot(dist4,'b',alpha=0.4)
    plt.plot(dist5,'orange',alpha=1)
    plt.plot(dist6,'b',alpha=0.4)
   # plt.plot(dist7,'b',alpha=0.4)
    plt.plot(dist8,'b',alpha=0.4)
    plt.plot(dist9,'b',alpha=0.4)
    plt.plot(dist10,'b',alpha=0.4)
  
    plt.ylabel('Distance')
    plt.xlabel('Frame')
    plt.grid(True)

    plt.xlim((0,140))
    plt.show()
    
    
    
    plt.tight_layout()
     

    #plt.show()
    
    #return plt.figure
    df = pd.DataFrame(np.array([dist1,dist2,dist3,dist4,dist5,dist6,dist7,dist8,dist9,dist10]))
    
    return df





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
    print(lag)
    com=[]
    ref=[]
    for i in range(np.size(data,1)):
        com.append(data.iloc[comi][i])
        ref.append(data.iloc[refi][i]) 
    difference=[]
    for i in path:
        difference.append(abs(com[i[0]]-ref[i[1]]))
    
    
    
#    plt.plot(data.iloc[refi],'g ',alpha=0.4)
#    plt.plot(data.iloc[comi],'b',alpha=0.4)
#      
#    plt.ylabel('Distance')
#    plt.xlabel('Frame')
#    plt.grid(True)

    #
    #mapp=[]
    dtwd=[]
    
    for i in range(len(data.iloc[refi])):
        x=i+lag[i]
        dtwd.append(data.iloc[comi][x])
    
    return dtwd

rankings=[3,5,2,1,10,8,9,4,6]
data=v1(3)    
refi=rankings[0]

#comi=2 

#dtwed=dtwd(data,refi,comi)
#plt.plot(dtwed,'r',alpha=0.4)
#plt.plot(data.iloc[refi],'g',alpha=0.4)
#plt.plot(data.iloc[comi],'b',alpha=0.4)
#plt.ylabel('Distance')
#plt.xlabel('Frame')
#plt.grid(True)
#plt.xlim((0,140))


dtwdlist=data[:]
for i in range(len(data)):
    dtwed=dtwd(data,refi,i)
    for j in range(np.size(data,1)):
        dtwdlist.iloc[i][j]=dtwed[j]
    

    
    plt.plot(data.iloc[i],'g',alpha=0.4)
     
plt.ylabel('Distance')
plt.xlabel('Frame')
plt.grid(True)
plt.xlim((0,140))
    
    
    
