# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:11:03 2020

@author: neilw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colour import Color
from scipy.signal import savgol_filter

#plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\1.json')

plot3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\3.json')
plot4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\4.json')
plot5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\5.json')
plot6= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\6.json')
plot7= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\7.json')
plot8= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\8.json')
plot9= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\9.json')
plot10= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\10.json')




#    #index mapping
bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
    
index=15
 
frames=np.shape(plot3)[1]
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

for i in range(frames):

    dist3.append(((plot3.iloc[dex][i][0])**2+(plot3.iloc[dex][i][1])**2+(plot3.iloc[dex][i][2])**2)**0.5)
    dist4.append(((plot4.iloc[dex][i][0])**2+(plot4.iloc[dex][i][1])**2+(plot4.iloc[dex][i][2])**2)**0.5)
    dist5.append(((plot5.iloc[dex][i][0])**2+(plot5.iloc[dex][i][1])**2+(plot5.iloc[dex][i][2])**2)**0.5)
    dist6.append(((plot6.iloc[dex][i][0])**2+(plot6.iloc[dex][i][1])**2+(plot6.iloc[dex][i][2])**2)**0.5)
    dist7.append(((plot7.iloc[dex][i][0])**2+(plot7.iloc[dex][i][1])**2+(plot7.iloc[dex][i][2])**2)**0.5)
    dist8.append(((plot8.iloc[dex][i][0])**2+(plot8.iloc[dex][i][1])**2+(plot8.iloc[dex][i][2])**2)**0.5)
    dist9.append(((plot9.iloc[dex][i][0])**2+(plot9.iloc[dex][i][1])**2+(plot9.iloc[dex][i][2])**2)**0.5)
    dist10.append(((plot10.iloc[dex][i][0])**2+(plot10.iloc[dex][i][1])**2+(plot10.iloc[dex][i][2])**2)**0.5)


dist4=np.subtract(dist4,dist3)
dist5=np.subtract(dist5,dist3)
dist6=np.subtract(dist6,dist3)
dist7=np.subtract(dist7,dist3)
dist8=np.subtract(dist8,dist3)
dist9=np.subtract(dist9,dist3)
dist10=np.subtract(dist10,dist3)


fig = plt.figure(figsize=(10, 5))
#fig, ax = plt.subplots()
#plt.plot([np.nan]*8+temp,'b')


plt.plot(dist4,'b')
plt.plot(dist5,'y')
plt.plot(dist6,'orange')
plt.plot(dist7,'purple')
plt.plot(dist8,'green')
plt.plot(dist9,'black')
plt.plot(dist10,'grey')

plt.ylabel('Distance')
plt.xlabel('Frame')
plt.grid(True)
#ax.set_axisbelow(True)
#ax.minorticks_on()
#ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlim((0,102))
plt.show()



plt.tight_layout()
 

plt.show()