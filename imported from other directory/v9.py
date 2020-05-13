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
    
index=16
 
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

    
#######################################Below this should be a function but for now just do x
#dist = savgol_filter(dist, 21, 3) # window size 51, polynomial order 3

dist3 = savgol_filter(dist3, 21, 3)  
dist4 = savgol_filter(dist4, 21, 3)  
dist5 = savgol_filter(dist5, 21, 3)  
dist6 = savgol_filter(dist6, 21, 3)  
dist7 = savgol_filter(dist7, 21, 3)  
dist8 = savgol_filter(dist8, 21, 3)  
dist9 = savgol_filter(dist9, 21, 3)  
dist10 = savgol_filter(dist10, 21, 3)  

temp=[]
temp3=[]
temp4=[]
temp5=[]
temp6=[]
temp7=[]
temp8=[]
temp9=[]
temp10=[]

for i in range(frames-1):
    
   # temp.append(dist[i+1]-dist[i])
    temp3.append(dist3[i+1]-dist3[i])
    temp4.append(dist4[i+1]-dist4[i])
    temp5.append(dist5[i+1]-dist5[i])
    temp6.append(dist6[i+1]-dist6[i])
    temp7.append(dist7[i+1]-dist7[i])
    temp8.append(dist8[i+1]-dist8[i])
    temp9.append(dist9[i+1]-dist9[i])
    temp10.append(dist10[i+1]-dist10[i])
        
    
temp4=np.subtract(temp4,temp3)
temp5=np.subtract(temp5,temp3)
temp6=np.subtract(temp6,temp3)
temp7=np.subtract(temp7,temp3)
temp8=np.subtract(temp8,temp3)
temp9=np.subtract(temp9,temp3)
temp10=np.subtract(temp10,temp3)



fig = plt.figure(figsize=(10, 5))
#fig, ax = plt.subplots()
#plt.plot([np.nan]*8+temp,'b')
plt.plot(temp4,'b')
plt.plot(temp5,'y')
plt.plot(temp6,'orange')
plt.plot(temp7,'purple')
plt.plot(temp8,'green')
plt.plot(temp9,'black')
plt.plot(temp10,'grey')

plt.ylabel('Speed')
plt.xlabel('Frame')
plt.grid(True)
#ax.set_axisbelow(True)
#ax.minorticks_on()
#ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlim((0,102))
plt.show()



plt.tight_layout()
 

plt.show()