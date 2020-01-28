# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:45:43 2020

@author: neilw
"""
from vpython import *
import pandas as pd
import numpy as np
from formatdata_length_constraint import format
from collections import Counter
from scipy.signal import correlate
from simulation_simul_vis import simv
from simulation_simul import sim
import matplotlib.pyplot as plt
import calc_vel_accel as deltas
import joint_angle as ja
import math
from colour import Color
import joint_angle as ja
from spherical import asSpherical
from spherical import asCartesian
import pickle


#    [0]  = 'Hip'   [1]  = 'RHip'   [2]  = 'RKnee'   [3]  = 'RFoot'   [6]  = 'LHip'   [7]  = 'LKnee'   [8]  = 'LFoot'   [12] = 'Spine'   [13] = 'Thorax'
#    [14] = 'Neck/Nose'   [15] = 'Head'   [17] = 'LShoulder'   [18] = 'LElbow'   [19] = 'LWrist'   [25] = 'RShoulder'   [26] = 'RElbow'   [27] = 'RWrist'

# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm

bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
limb_length=[124,452,504,124,452,504,252,231,78,112,120,250,230,120,250,230]


#formats data so that becomes matrix of dimensions. Rows are joints. Columns are frames. Also centres coords on hip
#data_f = format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1_3d_data.json',bones,joints,limb_length)
#data_f.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1formated.json')
#data_f_3= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3_3d_data.json',bones,joints,limb_length)
#data_f_3.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
#data_f_4= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4_3d_data.json',bones,joints,limb_length) 
#data_f_4.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4formated.json')
#data_f_5= format(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5_3d_data.json',bones,joints,limb_length) 
#data_f_5.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')


#load formated data instead
#data_f = pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF1formated.json')
data_f_3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
#data_f_4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF4formated.json')  
data_f_5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')  


frame=0

#df_v=dt.df_v(data_f_new)
#df_a=dt.df_a(df_v)
#scene2 = canvas()
#sim(frame,data_f_3,bones,joints,limb_length,vec(0,0,1))

scene=canvas()
scene.camera.pos=vector(1,-2000,0)
scene.camera.axis=vector(-1,+2000,0)
scene.up=vector(0,0,1)
scene.userzoom =True
scene.userspin=True
scene.width = scene.height = 1000
scene.background= color.white
distant_light(direction=vector( 0.88,  -0.44,  0.2),       color=color.gray(0.8))
scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.

"""
############################################################################

skeleton=[]
jeleton=[]

skeleton1=[]
jeleton1=[]

#for x correlation
A=[]
B=[]

#make sure time matches for each (to be corrected by xcorr eventually)
plot1=data_f_3.iloc[:,37:139]
plot1.columns = range(plot1.shape[1])

plot2=data_f_5.iloc[:,25:127]
plot2.columns = range(plot2.shape[1])

#for d lines
d_lines=[]

#simulation
while frame<max(np.shape(plot2)[1],np.shape(plot1)[1])-1:
    if frame<np.shape(plot1)[1]-1:
        temp=simv(skeleton,jeleton,frame,plot1,bones,joints,limb_length,vec(0,1,0),False,False,vec(1,1,1),1)
        skeleton=temp[0]
        jeleton=temp[1]
    if frame<np.shape(plot2)[1]-1:     
        temp2=sim(skeleton1,jeleton1,frame,plot2,bones,joints,limb_length,vec(1,0,0),False,False,vec(0.5,0.5,0.5))
        skeleton1=temp2[0]
        jeleton1=temp2[1]
        
    
    start=plot1[frame]
    end=plot2[frame]
    delta=np.subtract(end[joints[-1]],start[joints[-1]])
    start_temp=start[joints[-1]]
    
    #plot difference lines
#    red = Color("red")
#    colors = list(red.range_to(Color("white"),101))
#    rgbc=colors[frame].rgb
#    d_lines.append(cylinder(pos=vector(start_temp[0],start_temp[1],start_temp[2]), axis=vector(delta[0],delta[1],delta[2]), radius=2, color=vec(0,0,1)))
#    d_lines.append(sphere(pos=vector(start_temp[0],start_temp[1],start_temp[2]), radius=10,color=vector(rgbc[0],rgbc[1],rgbc[2])))
#    
    #plot axis
    arx=arrow(pos=vector(500,0,0),axis=vector(100,0,0),color=vec(1,0,0))
    ary=arrow(pos=vector(500,0,0),axis=vector(0,100,0),color=vec(0,1,0))
    arz=arrow(pos=vector(500,0,0),axis=vector(0,0,100),color=vec(0,0,1))
    
    
    
    #joint angle colouring
    angles1=ja.joint_angle(frame,plot1,bones,joints)  
    angles2=ja.joint_angle(frame,plot2,bones,joints) 
    angles=np.subtract(angles1,angles2)

    red = Color("blue")
    colors = list(red.range_to(Color("green"),70))
    
    for i in range(len(jeleton)):
        if angles[i]==0:
            jeleton[i].color=color.white
        else:
            rgbc=colors[abs(int(angles[i]))].rgb
            jeleton[i].color=vector(rgbc[0],rgbc[1],rgbc[2])

#    
#    #label right shoulder in polar coordinates length angle from vertical angle anticlockwise from red x axis
#    shoulderstart=np.subtract(start[joints[-2]],start[joints[-3]])
#    s_s=asSpherical(shoulderstart)
#    shoulderend=np.subtract(end[joints[-2]],end[joints[-3]])
#    s_send=asSpherical(shoulderend)
#    def res(y):
#        for x in range(len(y)):
#            if y[x]<0:
#                y[x]=360+y[x]             
#        return y
#
#    s_s=res(s_s)
#    s_send=res(s_send)
#    s_diff=np.subtract(s_send,s_s)
#    start_temp3=start[joints[-3]]
#    
#    #label right arm angle 
#    start_temp2=start[joints[-2]]
#
#    if frame ==0:
#        al=label(pos=vec(start_temp2[0],start_temp2[1],start_temp2[2]), text=int(angles1[15]), yoffset=-50)
#        adl=label(pos=vec(start_temp2[0],start_temp2[1],start_temp2[2]), text=int(angles[15]), yoffset=50, color=color.red)
#        dl=label(pos=vec(start_temp[0],start_temp[1],start_temp[2]), text='%d,%d,%d' % (start_temp[0],start_temp[1],start_temp[2]), yoffset=-50, box=False)
#        ddl=label(pos=vec(start_temp[0],start_temp[1],start_temp[2]),  text='%d,%d,%d' % (delta[0],delta[1],delta[2]), yoffset=50, color=color.red, box=False)
#        sdl=label(pos=vec(start_temp3[0],start_temp3[1],start_temp3[2]), text='%d,%d' % (s_diff[1],s_diff[2]), yoffset=50, color=color.red)
#        sl=label(pos=vec(start_temp3[0],start_temp3[1],start_temp3[2]), text='%d,%d' % (s_s[1],s_s[2]), yoffset=-50)
#    else:
#        #elbow
#        al.pos=vec(start_temp2[0],start_temp2[1],start_temp2[2])
#        al.text=int(angles1[15])
#        adl.pos=vec(start_temp2[0],start_temp2[1],start_temp2[2])
#        adl.text=int(angles[15])
#        
#        #hand
#        dl.pos=vec(start_temp[0],start_temp[1],start_temp[2])
#        dl.text= text='%d,%d,%d' % (start_temp[0],start_temp[1],start_temp[2])
#        
#        ddl.pos=vec(start_temp[0],start_temp[1],start_temp[2])
#        ddl.text= text='%d,%d,%d' % (delta[0],delta[1],delta[2])
#        
#        #shoulder
#        sdl.pos=vec(start_temp3[0],start_temp3[1],start_temp3[2])
#        sdl.text= text='%d,%d' % (s_diff[1],s_diff[2])
#        sl.pos=vec(start_temp3[0],start_temp3[1],start_temp3[2])
#        sl.text= text='%d,%d' % (s_s[1],s_s[2])   
         
    
    #graph
    
#        f1 = gdots(color=color.cyan)
#        f1.plot(pos=[frame,angles1[15]])
#        f2 = gdots(color=color.magenta)
#        f2.plot(pos=[frame,angles2[15]])
#        f3 = gdots(color=color.blue)
#        f3.plot(pos=[frame,float(s_s[2])])
#        f4 = gdots(color=color.yellow)
#        f4.plot(pos=[frame,float(s_send[2])])
#        f5 = gdots(color=color.red)
#        f5.plot(pos=[frame,float(s_s[1])])
#        f6 = gdots(color=color.green)
#        f6.plot(pos=[frame,float(s_send[1])])

#        f1 = gdots(color=color.red)
#        f1.plot(pos=[frame,start_temp[0]])
#        f2 = gdots(color=color.blue)
#        f2.plot(pos=[frame,start_temp[1]])
#        f3 = gdots(color=color.black)
#        f3.plot(pos=[frame,start_temp[2]])       
#diff
#        f1 = gdots(color=color.red)
#        f1.plot(pos=[frame,delta[0]])
#        f2 = gdots(color=color.blue)
#        f2.plot(pos=[frame,delta[1]])
#        f3 = gdots(color=color.black)
#        f3.plot(pos=[frame,delta[2]])     
     #cross correlation elbow angles
    
    
    A.append(angles1[15])
    B.append(angles2[15])    
   
    
 
        
        
    frame+=1
#plot 3d trace time color
scene2=canvas()
scene2.background=color.white
scene2.up=vector(0,0,1)
scene2.width = scene2.height = 1000
scene2.camera.pos=vector(1,-2000,2000)
scene2.camera.axis=vector(-1,+2000,-2000)
distant_light(direction=vector( 0.88,  -0.44,  0.2),       color=color.gray(0.8))
arx=arrow(pos=vector(500,0,0),axis=vector(100,0,0),color=vec(1,0,0))
ary=arrow(pos=vector(500,0,0),axis=vector(0,100,0),color=vec(0,1,0))
arz=arrow(pos=vector(500,0,0),axis=vector(0,0,100),color=vec(0,0,1))
#above
#scene2.width = scene2.height = 1000
#scene2.camera.pos=vector(1,-2000,2000)
#scene2.camera.axis=vector(-1,+2000,-2000)
frame=0
while frame<max(np.shape(plot2)[1],np.shape(plot1)[1])-1:
    red = Color("red")
    colors = list(red.range_to(Color("white"),101))
    rgbc=colors[frame].rgb
           
    a=(frame/max(np.shape(plot2)[1],np.shape(plot1)[1]))*0.9+0.1
    
    xyz=[]
    x=plot1[frame][joints[-1]][0]
    y=plot1[frame][joints[-1]][1]
    z=plot1[frame][joints[-1]][2]

    xyz.append(sphere(pos=vector(x,y,z), radius=10,color=vector(0.5,0.5,0.5)))
    frame+=1

#plot 3d trace time xy plane yz plane
#scene2=canvas()
#scene2.background=color.white
#scene2.up=vector(0,0,1)
#scene2.width = scene2.height = 1000
#scene2.camera.pos=vector(1,-2000,2000)
#scene2.camera.axis=vector(-1,+2000,-2000)
##above
##scene2.width = scene2.height = 1000
##scene2.camera.pos=vector(1,-2000,2000)
##scene2.camera.axis=vector(-1,+2000,-2000)
#frame=0
#arx=arrow(pos=vector(500,0,0),axis=vector(100,0,0),color=vec(1,0,0))
#ary=arrow(pos=vector(500,0,0),axis=vector(0,100,0),color=vec(0,1,0))
#arz=arrow(pos=vector(500,0,0),axis=vector(0,0,100),color=vec(0,0,1))
#while frame<max(np.shape(plot2)[1],np.shape(plot1)[1])-1:
#    
#    xyz=[]
#    x=plot1[frame][joints[-1]][0]
#    y=plot1[frame][joints[-1]][1]
#    z=frame*10
#
#    xyz.append(sphere(pos=vector(x,y,z), radius=10,color=color.red))
#    frame+=1

#scene.range = 1.8
scene.title = "Pose Visualisation"   

#deltas.df_v(plot1).to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\plot1rf3vel.json')
#deltas.df_a(plot1).to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\plot1rf3accel.json')
#deltas.df_v(plot1).to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\plot2rf5vel.json')
#deltas.df_a(plot1).to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\plot2rf5accel.json')
#plot1.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\plot1rf3.json')
#plot2.to_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\plot2rf5.json')