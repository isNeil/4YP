# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:45:43 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np


from scipy.signal import correlate
from simulation_simul import sim

import calc_vel_accel as delta
import joint_angle as ja

from colour import Color

from spherical import asSpherical
from spherical import asCartesian
from formatdata_length_constraint import format


#    [0]  = 'Hip'   [1]  = 'RHip'   [2]  = 'RKnee'   [3]  = 'RFoot'   [6]  = 'LHip'   [7]  = 'LKnee'   [8]  = 'LFoot'   [12] = 'Spine'   [13] = 'Thorax'
#    [14] = 'Neck/Nose'   [15] = 'Head'   [17] = 'LShoulder'   [18] = 'LElbow'   [19] = 'LWrist'   [25] = 'RShoulder'   [26] = 'RElbow'   [27] = 'RWrist'

# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm

bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
limb_length=[124,452,504,124,452,504,252,231,78,112,120,250,230,120,250,230]


#formats data so that becomes matrix of dimensions. Rows are joints. Columns are frames. Also centres coords on hip
data_f = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\jav1.json',bones,joints,limb_length)



frame=0

#df_v=dt.df_v(data_f_new)
#df_a=dt.df_a(df_v)
#scene2 = canvas()
#sim(frame,data_f_3,bones,joints,limb_length,vec(0,0,1))

scene=canvas()
scene.camera.pos=vector(1,-2000,0)
scene.camera.axis=vector(-1,+2000,0)
scene.up=vector(0,0,1)
scene.userzoom =False
scene.userspin=True
scene.width = scene.height = 1000
############################################################################

skeleton=[]
jeleton=[]

skeleton1=[]
jeleton1=[]

#for x correlation
A=[]
B=[]

#make sure time matches for each (to be corrected by xcorr eventually)
plot1=data_f

#for d lines
d_lines=[]

#simulation
while frame<np.shape(plot1)[1]-1:
    
    temp=sim(skeleton,jeleton,frame,plot1,bones,joints,limb_length,vec(0,1,0),True,False,vec(1,1,1),0)
    skeleton=temp[0]
    jeleton=temp[1]
    #plot axis
    arx=arrow(pos=vector(500,0,0),axis=vector(100,0,0),color=vec(1,0,0))
    ary=arrow(pos=vector(500,0,0),axis=vector(0,100,0),color=vec(0,1,0))
    arz=arrow(pos=vector(500,0,0),axis=vector(0,0,100),color=vec(0,0,1))
    
    

    
    #label right shoulder in polar coordinates length angle from vertical angle anticlockwise from red x axis
    shoulderstart=np.subtract(start[joints[-2]],start[joints[-3]])
    s_s=asSpherical(shoulderstart)
    shoulderend=np.subtract(end[joints[-2]],end[joints[-3]])
    s_send=asSpherical(shoulderend)
    def res(y):
        for x in range(len(y)):
            if y[x]<0:
                y[x]=360+y[x]             
        return y

    s_s=res(s_s)
    s_send=res(s_send)
    s_diff=np.subtract(s_send,s_s)
    start_temp3=start[joints[-3]]
    
    #label right arm angle 
    start_temp2=start[joints[-2]]

    if frame ==0:
        al=label(pos=vec(start_temp2[0],start_temp2[1],start_temp2[2]), text=int(angles1[15]), yoffset=-50)
        adl=label(pos=vec(start_temp2[0],start_temp2[1],start_temp2[2]), text=int(angles[15]), yoffset=50, color=color.red)
        dl=label(pos=vec(start_temp[0],start_temp[1],start_temp[2]), text='%d,%d,%d' % (start_temp[0],start_temp[1],start_temp[2]), yoffset=-50, box=False)
        ddl=label(pos=vec(start_temp[0],start_temp[1],start_temp[2]),  text='%d,%d,%d' % (delta[0],delta[1],delta[2]), yoffset=50, color=color.red, box=False)
        sdl=label(pos=vec(start_temp3[0],start_temp3[1],start_temp3[2]), text='%d,%d' % (s_diff[1],s_diff[2]), yoffset=50, color=color.red)
        sl=label(pos=vec(start_temp3[0],start_temp3[1],start_temp3[2]), text='%d,%d' % (s_s[1],s_s[2]), yoffset=-50)
    else:
        
        al.pos=vec(start_temp2[0],start_temp2[1],start_temp2[2])
        al.text=int(angles1[15])
        adl.pos=vec(start_temp2[0],start_temp2[1],start_temp2[2])
        adl.text=int(angles[15])
        dl.pos=vec(start_temp[0],start_temp[1],start_temp[2])
        dl.text= text='%d,%d,%d' % (start_temp[0],start_temp[1],start_temp[2])
        ddl.pos=vec(start_temp[0],start_temp[1],start_temp[2])
        ddl.text= text='%d,%d,%d' % (delta[0],delta[1],delta[2])
        sdl.pos=vec(start_temp3[0],start_temp3[1],start_temp3[2])
        sdl.text= text='%d,%d' % (s_diff[1],s_diff[2])
        sl.pos=vec(start_temp3[0],start_temp3[1],start_temp3[2])
        sl.text= text='%d,%d' % (s_s[1],s_s[2])   
         
    
    #graph
    
    f1 = gdots(color=color.cyan)
    f1.plot(pos=[frame,angles1[15]])
    f2 = gdots(color=color.magenta)
    f2.plot(pos=[frame,angles2[15]])
    f3 = gdots(color=color.blue)
    f3.plot(pos=[frame,float(s_s[2])])
    f4 = gdots(color=color.yellow)
    f4.plot(pos=[frame,float(s_send[2])])
    f5 = gdots(color=color.red)
    f5.plot(pos=[frame,float(s_s[1])])
    f6 = gdots(color=color.green)
    f6.plot(pos=[frame,float(s_send[1])])
      
     #cross correlation elbow angles
    
    
    A.append(angles1[15])

   
    

        
        
    frame+=1


#xcorr
nsamples = len(A)

# regularize datasets by subtracting mean and dividing by s.d.
A -= np.mean(A); A /= np.std(A)
B -= np.mean(B); B /= np.std(B)

# Find cross-correlation
xcorr = correlate(A, B)

# delta time array to match xcorr
dt = np.arange(1-nsamples, nsamples)

recovered_time_shift = dt[np.argmax(xcorr)]

print( "Recovered time shift: %d" % (recovered_time_shift))





#scene.range = 1.8
scene.title = "Pose Visualisation"   
