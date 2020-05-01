# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:11:03 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from colour import Color
import time

def v1(index):

    #plot3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
    #plot4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4formated.json')
    #plot5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')
    #plot6=pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\rf6formated.json')
    #plot7=pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\rf7formated.json')
    #plot8=pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\rf8formated.json')
    #plot9=pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\rf9formated.json')
    #plot10=pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\rf10formated.json')
    
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
        
    index=16
     
    #joint 0 to 27 Rwrist
    #dist=[]
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
    for i in range(np.shape(plot3)[1]):
        dist3.append(((plot3.iloc[dex][i][0])**2+(plot3.iloc[dex][i][1])**2+(plot3.iloc[dex][i][2])**2)**0.5)    
    for i in range(np.shape(plot4)[1]):    
        dist4.append(((plot4.iloc[dex][i][0])**2+(plot4.iloc[dex][i][1])**2+(plot4.iloc[dex][i][2])**2)**0.5)
    for i in range(np.shape(plot5)[1]): 
        dist5.append(((plot5.iloc[dex][i][0])**2+(plot5.iloc[dex][i][1])**2+(plot5.iloc[dex][i][2])**2)**0.5)
    for i in range(np.shape(plot6)[1]):    
        dist6.append(((plot6.iloc[dex][i][0])**2+(plot6.iloc[dex][i][1])**2+(plot6.iloc[dex][i][2])**2)**0.5)
    for i in range(np.shape(plot7)[1]):
        dist7.append(((plot7.iloc[dex][i][0])**2+(plot7.iloc[dex][i][1])**2+(plot7.iloc[dex][i][2])**2)**0.5)
    for i in range(np.shape(plot9)[1]):
        dist9.append(((plot9.iloc[dex][i][0])**2+(plot9.iloc[dex][i][1])**2+(plot9.iloc[dex][i][2])**2)**0.5)
    for i in range(np.shape(plot10)[1]):
        dist10.append(((plot10.iloc[dex][i][0])**2+(plot10.iloc[dex][i][1])**2+(plot10.iloc[dex][i][2])**2)**0.5)
    for i in range(np.shape(plot8)[1]):    
        dist8.append(((plot8.iloc[dex][i][0])**2+(plot8.iloc[dex][i][1])**2+(plot8.iloc[dex][i][2])**2)**0.5)
        
    #######################################Below this should be a function but for now just do x
    
    
#    #fig, ax = plt.subplots()
#    #plt.plot([np.nan]*8+dist,"b")
#    
#    fig = plt.figure(figsize=(10, 3))
#    #plt.plot(dist4[15:117],'b')
#    #plt.plot(dist5[28:130],'y')
#    #plt.plot(dist6[98:200],'orange')
#    #plt.plot(dist7[57:159],'purple')
#    #plt.plot(dist8[64:166],'g')
#    #plt.plot(dist9,'black')
#    #plt.plot(dist10[77:179],'grey')
#    #plt.plot(dist3[41:143],"r")
#    
#    
#    plt.plot(dist4,'b',alpha=0.4)
#    plt.plot(dist5,'b',alpha=0.4)
#    plt.plot(dist6,'b',alpha=0.4)
#    plt.plot(dist7,'b',alpha=0.4)
#    plt.plot(dist8,'b',alpha=0.4)
#    plt.plot(dist9,'b',alpha=0.4)
#    plt.plot(dist10,'b',alpha=0.4)
#    plt.plot(dist3,"r")
#
#    plt.ylabel('Distance')
#    plt.xlabel('Frame')
#    plt.grid(True)
#
#    plt.xlim((0,102))
#    plt.show()
#    
#    
#    
#    plt.tight_layout()
#     

    #plt.show()
    
    #return plt.figure
    df = pd.DataFrame(np.array([dist3,dist4,dist5,dist6,dist7,dist8,dist9,dist10]))
    
    return df

#
#df=v1(16)
#print(df.iloc[0,:].values.tolist())

    
    
    
    
    
    
    
    #save 102 frame data
    ##
    #plot3=plot3.iloc[:,41:143]
    #plot3.columns = range(plot3.shape[1])
    #plot3.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\3.json')
    ##
    #plot4=plot4.iloc[:,15:117]
    #plot4.columns = range(plot4.shape[1])
    #plot4.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\4.json')
    #
    #plot5=plot5.iloc[:,28:130]
    #plot5.columns = range(plot5.shape[1])
    #plot5.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\5.json')
    #
    #plot6=plot6.iloc[:,98:200]
    #plot6.columns = range(plot6.shape[1])
    #plot6.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\6.json')
    #
    #plot7=plot7.iloc[:,57:159]
    #plot7.columns= range(plot7.shape[1])
    #plot7.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\7.json')
    ###
    #plot8=plot8.iloc[:,64:166]
    #plot8.columns= range(plot8.shape[1])
    #plot8.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\8.json')
    ##
    
#    plot9=plot9.iloc[:,0:102]
#    plot9.columns= range(plot8.shape[1])    
#    
#    plot9.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\9.json')
    
    
    
    #
    #plot10=plot10.iloc[:,77:179]
    #plot10.columns=range(plot10.shape[1])
    #plot10.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\10.json')
    ##
