# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:11:03 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import savgol_filter

def v3(index):
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
    #bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
        

     
    frames=np.shape(plot3)[1]
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
    
    for i in range(frames):
        dist1.append(((plot1.iloc[dex][i][0])**2+(plot1.iloc[dex][i][1])**2+(plot1.iloc[dex][i][2])**2)**0.5)    
        dist2.append(((plot2.iloc[dex][i][0])**2+(plot2.iloc[dex][i][1])**2+(plot2.iloc[dex][i][2])**2)**0.5)    
        dist3.append(((plot3.iloc[dex][i][0])**2+(plot3.iloc[dex][i][1])**2+(plot3.iloc[dex][i][2])**2)**0.5)
        dist4.append(((plot4.iloc[dex][i][0])**2+(plot4.iloc[dex][i][1])**2+(plot4.iloc[dex][i][2])**2)**0.5)
        dist5.append(((plot5.iloc[dex][i][0])**2+(plot5.iloc[dex][i][1])**2+(plot5.iloc[dex][i][2])**2)**0.5)
        dist6.append(((plot6.iloc[dex][i][0])**2+(plot6.iloc[dex][i][1])**2+(plot6.iloc[dex][i][2])**2)**0.5)
        dist7.append(((plot7.iloc[dex][i][0])**2+(plot7.iloc[dex][i][1])**2+(plot7.iloc[dex][i][2])**2)**0.5)
        dist8.append(((plot8.iloc[dex][i][0])**2+(plot8.iloc[dex][i][1])**2+(plot8.iloc[dex][i][2])**2)**0.5)
        dist9.append(((plot9.iloc[dex][i][0])**2+(plot9.iloc[dex][i][1])**2+(plot9.iloc[dex][i][2])**2)**0.5)
        dist10.append(((plot10.iloc[dex][i][0])**2+(plot10.iloc[dex][i][1])**2+(plot10.iloc[dex][i][2])**2)**0.5)
    
        
    #######################################Below this should be a function but for now just do x
    #dist = savgol_filter(dist, 21, 3) # window size 51, polynomial order 3
    dist1 = savgol_filter(dist1, 21, 3)
    dist2 = savgol_filter(dist2, 21, 3)  
    dist3 = savgol_filter(dist3, 21, 3)  
    dist4 = savgol_filter(dist4, 21, 3)  
    dist5 = savgol_filter(dist5, 21, 3)  
    dist6 = savgol_filter(dist6, 21, 3)  
    dist7 = savgol_filter(dist7, 21, 3)  
    dist8 = savgol_filter(dist8, 21, 3)  
    dist9 = savgol_filter(dist9, 21, 3)  
    dist10 = savgol_filter(dist10, 21, 3)  
    
    speed1=[]
    speed2=[]
    speed3=[]
    speed4=[]
    speed5=[]
    speed6=[]
    speed7=[]
    speed8=[]
    speed9=[]
    speed10=[]
    
    
    
    for i in range(frames-1):
        speed1.append(dist1[i+1]-dist1[i])
        speed2.append(dist2[i+1]-dist2[i])
        speed3.append(dist3[i+1]-dist3[i])
        speed4.append(dist4[i+1]-dist4[i])
        speed5.append(dist5[i+1]-dist5[i])
        speed6.append(dist6[i+1]-dist6[i])
        speed7.append(dist7[i+1]-dist7[i])
        speed8.append(dist8[i+1]-dist8[i])
        speed9.append(dist9[i+1]-dist9[i])
        speed10.append(dist10[i+1]-dist10[i])
    
    speed1 = savgol_filter(speed1, 21, 3)  
    speed2 = savgol_filter(speed2, 21, 3)
    speed3 = savgol_filter(speed3, 21, 3)  
    speed4 = savgol_filter(speed4, 21, 3)  
    speed5 = savgol_filter(speed5, 21, 3)  
    speed6 = savgol_filter(speed6, 21, 3)  
    speed7 = savgol_filter(speed7, 21, 3)  
    speed8 = savgol_filter(speed8, 21, 3)  
    speed9 = savgol_filter(speed9, 21, 3)  
    speed10 = savgol_filter(speed10, 21, 3)  
    
    accel1=[]
    accel2=[]
    accel3=[]
    accel4=[]
    accel5=[]
    accel6=[]
    accel7=[]
    accel8=[]
    accel9=[]
    accel10=[]
    
    for i in range(frames-2):
        accel1.append(speed1[i+1]-speed1[i])
        accel2.append(speed2[i+1]-speed2[i])
        accel3.append(speed3[i+1]-speed3[i])
        accel4.append(speed4[i+1]-speed4[i])
        accel5.append(speed5[i+1]-speed5[i])
        accel6.append(speed6[i+1]-speed6[i])
        accel7.append(speed7[i+1]-speed7[i])
        accel8.append(speed8[i+1]-speed8[i])
        accel9.append(speed9[i+1]-speed9[i])
        accel10.append(speed10[i+1]-speed10[i])
    

    
#    plt.plot(accel1,"b",alpha=0.4)
#    plt.plot(accel2,"y",alpha=1)
#    plt.plot(accel3,"r",alpha=1) 
#    plt.plot(accel4,'b',alpha=0.4)
#    plt.plot(accel5,'orange',alpha=1)
#    plt.plot(accel6,'b',alpha=0.4)
#    #plt.plot(accel7,'b',alpha=0.4)
#    plt.plot(accel8,'b',alpha=0.4)
#    plt.plot(accel9,'b',alpha=0.4)
#    plt.plot(accel10,'b',alpha=0.4)
#  
#    plt.ylabel('Acceleration')
#    plt.xlabel('Frame')
#    plt.grid(True)
#
#    plt.xlim((0,140))
#    plt.show()
#    
#    
#    
#    plt.tight_layout()
     
    df = pd.DataFrame(np.array([accel1,accel2,accel3,accel4,accel5,accel6,accel7,accel8,accel9,accel10]))
    

    
    
    return df
#
#df=v3(1) #hip
#df=v3(2) #knee
#df=v3(3) #foot
#df=v3(7) #spine
#df=v3(8) #thorax
#df=v3(9) #nose
#df=v3(10) #head
#df=v3(14) #shoulder 
#df=v3(15) #arm
#df=v3(16) #wrsit