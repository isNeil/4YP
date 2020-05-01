# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:35:36 2020

@author: neilw
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from colour import Color

from operator import add

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
    dist3.append(((plot3.iloc[dex][i][0])**2+(plot3.iloc[dex][i][1])**2+(plot3.iloc[dex][i][2])**2)**0.5)    
for i in range(np.shape(plot3)[1]):
    dist3p.append(((plot3.iloc[dex-1][i][0])**2+(plot3.iloc[dex-1][i][1])**2+(plot3.iloc[dex-1][i][2])**2)**0.5)    

for i in range(np.shape(plot4)[1]):    
    dist4.append(((plot4.iloc[dex][i][0])**2+(plot4.iloc[dex][i][1])**2+(plot4.iloc[dex][i][2])**2)**0.5)
for i in range(np.shape(plot4)[1]):    
    dist4p.append(((plot4.iloc[dex-1][i][0])**2+(plot4.iloc[dex-1][i][1])**2+(plot4.iloc[dex-1][i][2])**2)**0.5)

for i in range(np.shape(plot5)[1]): 
    dist5.append(((plot5.iloc[dex][i][0])**2+(plot5.iloc[dex][i][1])**2+(plot5.iloc[dex][i][2])**2)**0.5)
for i in range(np.shape(plot5)[1]): 
    dist5p.append(((plot5.iloc[dex-1][i][0])**2+(plot5.iloc[dex-1][i][1])**2+(plot5.iloc[dex-1][i][2])**2)**0.5)

for i in range(np.shape(plot6)[1]):    
    dist6.append(((plot6.iloc[dex][i][0])**2+(plot6.iloc[dex][i][1])**2+(plot6.iloc[dex][i][2])**2)**0.5)
for i in range(np.shape(plot6)[1]):    
    dist6p.append(((plot6.iloc[dex-1][i][0])**2+(plot6.iloc[dex-1][i][1])**2+(plot6.iloc[dex-1][i][2])**2)**0.5)

for i in range(np.shape(plot7)[1]):
    dist7.append(((plot7.iloc[dex][i][0])**2+(plot7.iloc[dex][i][1])**2+(plot7.iloc[dex][i][2])**2)**0.5)
for i in range(np.shape(plot7)[1]):
    dist7p.append(((plot7.iloc[dex-1][i][0])**2+(plot7.iloc[dex-1][i][1])**2+(plot7.iloc[dex-1][i][2])**2)**0.5)


for i in range(np.shape(plot8)[1]):    
    dist8.append(((plot8.iloc[dex][i][0])**2+(plot8.iloc[dex][i][1])**2+(plot8.iloc[dex][i][2])**2)**0.5)
for i in range(np.shape(plot8)[1]):    
    dist8p.append(((plot8.iloc[dex-1][i][0])**2+(plot8.iloc[dex-1][i][1])**2+(plot8.iloc[dex-1][i][2])**2)**0.5)
        
   
for i in range(np.shape(plot9)[1]):
    dist9.append(((plot9.iloc[dex][i][0])**2+(plot9.iloc[dex][i][1])**2+(plot9.iloc[dex][i][2])**2)**0.5)
for i in range(np.shape(plot9)[1]):
    dist9p.append(((plot9.iloc[dex-1][i][0])**2+(plot9.iloc[dex-1][i][1])**2+(plot9.iloc[dex-1][i][2])**2)**0.5)


for i in range(np.shape(plot10)[1]):
    dist10.append(((plot10.iloc[dex][i][0])**2+(plot10.iloc[dex][i][1])**2+(plot10.iloc[dex][i][2])**2)**0.5)
for i in range(np.shape(plot10)[1]):
    dist10p.append(((plot10.iloc[dex-1][i][0])**2+(plot10.iloc[dex-1][i][1])**2+(plot10.iloc[dex-1][i][2])**2)**0.5)

 
######################################Below this should be a function but for now just do x




fig = plt.figure(figsize=(10, 3))


#plt.plot(dist4,'b',alpha=0.4)
#    plt.plot(dist5,'b',alpha=0.4)
#    plt.plot(dist6,'b',alpha=0.4)
#    plt.plot(dist7,'b',alpha=0.4)
#    plt.plot(dist8,'b',alpha=0.4)
#    plt.plot(dist9,'b',alpha=0.4)
#    plt.plot(dist10,'b',alpha=0.4)

def plot(dist3,dist3p,color,space):
    
    
    for i in range(len(dist3)):
        y=[dist3[i],dist3p[i]]
        x=[i+space,i+space]

        plt.plot(x,y, color, alpha=0.4)

    
    
    
    
#plot(dist3,dist3p,"r",0)
#plot(dist4,dist4p,"g",0.2)
#plot(dist5,dist5p,"b",0.4)
#plot(dist6,dist6p,"y",0.6)
#plot(dist7,dist7p,"purple",0.8)
##plot(dist8,dist8p,"black",0.7)
##plot(dist9,dist9p,"grey",0.8)
##plot(dist10,dist10p,"orange",0.9)
        
plot(dist3,dist3p,"r",0)
plot(dist4,dist4p,"blue",0)
#plot(dist6,dist6p,"y",0)



plt.ylabel('Distance')
plt.xlabel('Frame')
plt.grid(True)

plt.xlim((0,102))
plt.show()



 

plt.show()

#return plt.figure
#    df = pd.DataFrame(np.array([dist3,dist4,dist5,dist6,dist7,dist8,dist9,dist10]))

#    return #df
#
#v15()


    
    
    
