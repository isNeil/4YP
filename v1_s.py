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

#plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand1formated.json')
#plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand2formated.json')
#plot3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand3formated.json')
#plot4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand4formated.json')
#plot5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand5formated.json')
#plot6= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand6formated.json')
#plot7= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand7formated.json')
#plot8= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand8formated.json')
#plot9= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand9formated.json')
#plot10= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\stand10formated.json')


#selecting and saving frames

#plot1= plot1.iloc[:,15:156]
#plot1.columns = range(plot1.shape[1])
#
#plot2= plot2.iloc[:,11:152]
#plot2.columns = range(plot2.shape[1])
#
#plot3= plot3.iloc[:,22:163]
#plot3.columns = range(plot3.shape[1])
#
#plot4= plot4.iloc[:,13:154]
#plot4.columns = range(plot4.shape[1])
#plot5= plot5.iloc[:,26:167]
#plot5.columns = range(plot5.shape[1])
#plot6= plot6.iloc[:,21:162]
#plot6.columns = range(plot6.shape[1])
#plot7= plot7.iloc[:,0:141]
#plot7.columns = range(plot7.shape[1])
#plot8= plot8.iloc[:,18:159]
#plot8.columns = range(plot8.shape[1])
#plot9=plot9.iloc[:,18:159]
#plot9.columns = range(plot9.shape[1])
#plot10=plot10.iloc[:,18:159]
#plot10.columns = range(plot10.shape[1])

#plot1.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\1.json')
#plot2.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\2.json')
#plot3.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\3.json')
#plot4.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\4.json')
#plot5.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\5.json')
#plot6.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\6.json')
#plot7.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\7.json')
#plot8.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\8.json')
#plot9.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\9.json')
#plot10.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\140\10.json')







#    #index mapping
bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
    
index=3
 
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

diff=[]
#mapping index to joint 
dex=joints[index]


#for i in range(np.shape(plot1)[1]):
#    dist.append(((plot1.iloc[dex][i][0])**2+(plot1.iloc[dex][i][1])**2+(plot1.iloc[dex][i][2])**2)**0.5)
for i in range(np.shape(plot1)[1]):
    dist1.append(((plot1.iloc[dex][i][0])**2+(plot1.iloc[dex][i][1])**2+(plot1.iloc[dex][i][2])**2)**0.5)    

for i in range(np.shape(plot2)[1]):
    dist2.append(((plot2.iloc[dex][i][0])**2+(plot2.iloc[dex][i][1])**2+(plot2.iloc[dex][i][2])**2)**0.5)    

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


fig = plt.figure(figsize=(10, 3))

plt.plot(dist4,'b')
plt.plot(dist5,'y')
plt.plot(dist6,'orange')
plt.plot(dist7,'purple')
plt.plot(dist8,'g')
plt.plot(dist9,'black')
plt.plot(dist10,'grey')
plt.plot(dist3,"r")
plt.plot(dist1,"aqua")
plt.plot(dist2,"pink")

plt.ylabel('Distance')
plt.xlabel('Frame')
plt.grid(True)
#ax.set_axisbelow(True)
#ax.minorticks_on()
#ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlim((0,140))
plt.show()



plt.tight_layout()
 

#plt.show()

#return plt.figure




