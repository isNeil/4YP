# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:11:03 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




def v17(index):
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
    

    #mapping index to joint 
    dex=joints[index]
    
    
    #for i in range(np.shape(plot1)[1]):
    #    dist.append(((plot1.iloc[dex][i][0])**2+(plot1.iloc[dex][i][1])**2+(plot1.iloc[dex][i][2])**2)**0.5)
    
    
    
    for i in range(np.shape(plot1)[1]):
        dist1.append(plot1.iloc[dex][i][1])
        dist2.append(plot2.iloc[dex][i][1]) 
        dist3.append(plot3.iloc[dex][i][1])
        dist4.append(plot4.iloc[dex][i][1])
        dist5.append(plot5.iloc[dex][i][1])
        dist6.append(plot6.iloc[dex][i][1])
        dist7.append(plot7.iloc[dex][i][1])
        dist8.append(plot8.iloc[dex][i][1])
        dist9.append(plot9.iloc[dex][i][1])
        dist10.append(plot10.iloc[dex][i][1])
        
        
    #######################################Below this should be a function but for now just do x
    
    
    #fig, ax = plt.subplots()
    #plt.plot([np.nan]*8+dist,"b")
#    
#    fig = plt.figure(figsize=(10, 3))
#
##    plt.plot(dist1,"r",alpha=0.4)
##    plt.plot(dist2,"b",alpha=0.4)
##    plt.plot(dist3,"y",alpha=0.4) 
##    plt.plot(dist4,'g',alpha=0.4)
##    plt.plot(dist5,'purple',alpha=0.4)
##    plt.plot(dist6,'orange',alpha=0.4)
##    plt.plot(dist7,'pink',alpha=0.4)
##    plt.plot(dist8,'black',alpha=0.4)
##    plt.plot(dist9,'grey',alpha=0.4)
##    plt.plot(dist10,'brown',alpha=0.4)
#
##top 5 shown in blue, best in green, bottom 5 in red, worst black
##    plt.plot(dist1,"b",alpha=0.4)
##    plt.plot(dist2,"b",alpha=0.4)
##    plt.plot(dist3,"g",alpha=0.4) 
##    plt.plot(dist4,'r',alpha=0.4)
##    plt.plot(dist5,'b',alpha=0.4)
##    plt.plot(dist6,'black',alpha=0.4)
##    plt.plot(dist7,'r',alpha=0.4)
##    plt.plot(dist8,'r',alpha=0.4)
##    plt.plot(dist9,'r',alpha=0.4)
##    plt.plot(dist10,'b',alpha=0.4)
##  
#    
#    plt.plot(dist1,"b",alpha=0.4)
#    plt.plot(dist2,"yellow",alpha=1)
#    plt.plot(dist3,"red",alpha=1) 
#    plt.plot(dist4,'b',alpha=0.4)
#    plt.plot(dist5,'orange',alpha=1)
#    plt.plot(dist6,'b',alpha=0.4)
#  #  plt.plot(dist7,'pink',alpha=0.4)
#    plt.plot(dist8,'b',alpha=0.4)
#    plt.plot(dist9,'b',alpha=0.4)
#    plt.plot(dist10,'b',alpha=0.4)
#  
#    plt.ylabel('Distance')
#    plt.xlabel('Frame')
#    plt.grid(True)
#
#    plt.xlim((0,140))
#    plt.show()
#    
#    
#    
#    plt.tight_layout()
#     
#
#    #plt.show()
#    
    #return plt.figure
    df = pd.DataFrame(np.array([dist1,dist2,dist3,dist4,dist5,dist6,dist7,dist8,dist9,dist10]))
    
    return df

#right side first
#df=v1(1) #hip
#df=v1(4)
#df=v1(2) #knee
#df=v1(5)
#df=v1(3) #foot
#df=v1(6)
#df=v1(7) #spine
#df=v1(8) #thorax
#df=v1(9) #nose
#df=v1(10) #head
#df=v1(14) #shoulder
#df=v1(11) 
#df=v1(15) #arm
#df=v1(12)
#df=v1(16) #wrsit
#df=v1(13)
##print(df.iloc[0,:].values.tolist())

    
    
    
    
    
    
    
