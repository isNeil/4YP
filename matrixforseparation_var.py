# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 01:49:34 2020

@author: neilw
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pickle
from matplotlib import cm
from dtw_combined2 import dtwrecon
from dtw_combined2 import dtwhighlight
from v1f import v1
from v2f import v2
from v3f import v3
from v6f import v6
from v5f import v5
from v10f import v10
from v4f import v4
from v11f import v11
from v15f import v15
from v16f import v16
from v17f import v17
from v18f import v18

top=[3,5,2]
bott=[1,10,8,9,4,6]

joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
functions = [v1,v2,v3,v4,v5,v6,v16,v17,v18]
#output_var=[]
#output_mean=[]
#for func in functions:
#    
#    for i in range(len(joints)):
#        dtwdlist=dtwrecon(top,func(i))
#        [chose_times_mean,chose_times_var,allstats,differences_mean,differences_var]=dtwhighlight(top,bott,dtwdlist)
##        flat_differences = [item for sublist in l for item in sublist]
#        output_mean.append(sum(differences_mean))
#        output_var.append(sum(differences_var))
#
#
#
#
#pickle.dump([output_mean,output_var], open("output.p", "wb"))

output_mean,output_var = pickle.load(open("output.p","rb"))

a_mean = np.array(output_mean)
a_var = np.array(output_var)


ind_mean = np.argpartition(a_mean, -5)[-5:]
ind_var= np.argpartition(a_var,-5)[-5:]
a_mean[ind_mean]
a_var[ind_var]



output_var_formatted=[]
eachmeasure=[]
for j in range(len(functions)):
    for i in range(17):
        eachmeasure.append(output_var[i+j*17])
        
    output_var_formatted.append(eachmeasure)  
    eachmeasure=[]

print(output_var_formatted)  
df = pd.DataFrame(output_var_formatted) 

df=df[[1,4,2,5,3,6,7,8,9,10,14,11,15,12,16,13]]

df = df.drop([df.index[1] , df.index[2],df.index[4] , df.index[5] ])
#df.to_json(r'C:\Users\neilw\Desktop\420varformated.json')
output_var_formatted=df.values.tolist()
#output_mean_formatted= pd.read_json(r'C:\Users\neilw\Desktop\420formated.json')

plt.figure(0)
viridis = cm.get_cmap('binary', 256)
newcolors = viridis(np.linspace(0, 1, 256))

cmap = matplotlib.colors.ListedColormap(newcolors, name='colors', N=None)


fig, ax = plt.subplots(1,1,figsize=(13, 7.5))

img = ax.imshow(output_var_formatted, cmap=cmap)


x_label_list = [ 'R. Hip', 'L. Hip', 'R. Knee', 'L. Knee', 'R. Foot', 'L. Foot', 'Spine', 'Thorax', 'Neck', 'Head', 'R. Arm', 'L. Arm', 'R. Elbow', 'L. Elbow', 'R. Wrist', 'L. Wrist']

ax.set_xticks(range(17))

ax.set_xticklabels(x_label_list)
y_label_list = ['Distance', 'Angle', 'X axis Displacement', 'Y axis Displacement','Z axis Displacement' ]


ax.set_yticks(range(np.size(df,0)))

ax.set_yticklabels(y_label_list)



#
#fig.savefig("Images/MEASUREmatrixVAR.jpg", dpi=200) 

#import pylab as pl
#import numpy as np
#plt.figure(1)
#
#a = np.array([[0,43]])
#pl.figure(figsize=(15, 1))
#img = pl.imshow(a, cmap="binary")
#pl.gca().set_visible(False)
#cax = pl.axes([0.1, 0.2, 0.8, 0.6])
#pl.colorbar(orientation='horizontal', cax=cax)
#pl.savefig("Images/colorbarvar.jpg", dpi=200)
#

