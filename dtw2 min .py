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
    #print(lag)
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




def dtwrecon(top,vdata):
    #top are the plots you want to cluster, top and bott should be in descending performance
    #top=[3,5,2]
    #bott=[1,10,8,9,4,6]
    
    data=vdata.copy()
    refi=top[0]
    
    
    #comi=2 
    
    #dtwed=dtwd(data,refi,comi)
    #plt.plot(dtwed,'r',alpha=0.4)
    #plt.plot(data.iloc[refi],'g',alpha=0.4)
    #plt.plot(data.iloc[comi],'b',alpha=0.4)
    #plt.ylabel('Distance')
    #plt.xlabel('Frame')
    #plt.grid(True)
    #plt.xlim((0,140))
    
    
    dtwdlist=data.copy()
    
    
    for i in range(len(data)):
        dtwed=dtwd(data,refi,i)
        for j in range(np.size(data,1)):
            dtwdlist.iloc[i][j]=dtwed[j]
        
    
        
        plt.plot(dtwdlist.iloc[i],'g',alpha=0.4)
         
        
    plt.ylabel('Distance')
    plt.xlabel('Frame')
    plt.grid(True)
    plt.xlim((0,140))
    
    return dtwdlist

    
def dtwhighlight(top,bott,dtwdlist):  

    frame_good=[]
    frame_bad=[]
        
    
    separation=[]
    norm_dtwdlist=dtwdlist.copy()
    
    for i in range(np.size(dtwdlist,1)): 
        minval=min(dtwdlist.iloc[:][i])
        rang=max(dtwdlist.iloc[:][i])-minval
        for j in range(len(dtwdlist)):
            norm_dtwdlist.iloc[j][i]=(dtwdlist.iloc[j][i]-minval)/rang
        
        
        for j in top:
            frame_good.append(norm_dtwdlist.iloc[j-1][i])
        mean_good=np.mean(frame_good)
        for k in bott:
       
            frame_bad.append(norm_dtwdlist.iloc[k-1][i])
        mean_bad=np.mean(frame_bad)
        separation.append(abs(mean_good-mean_bad))
        
    
    separation_sorted=sorted(separation)
    
    cutoff=separation_sorted[int(np.floor(len(separation)*0.8))]
    
    chose_times=[]
    for i in range(len(separation)):
        if separation[i] > cutoff:
            chose_times.append(i)
    
    for i in chose_times:
        plt.axvspan(i, i+1, facecolor='grey', alpha=0.5)
    
    return chose_times

top=[3,5,2]
bott=[1,10,8,9,4,6]

dtwdlist=dtwrecon(top,v1(3))
dtwhighlight(top,bott,dtwdlist)


#raw = 'asdfa3fa'
#functions = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
#isanything = [func(raw) for func in functions]
#print repr(isanything)