# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:14:39 2020

@author: neilw
"""

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
import vis


#    [0]  = 'Hip'   [1]  = 'RHip'   [2]  = 'RKnee'   [3]  = 'RFoot'   [6]  = 'LHip'   [7]  = 'LKnee'   [8]  = 'LFoot'   [12] = 'Spine'   [13] = 'Thorax'
#    [14] = 'Neck/Nose'   [15] = 'Head'   [17] = 'LShoulder'   [18] = 'LElbow'   [19] = 'LWrist'   [25] = 'RShoulder'   [26] = 'RElbow'   [27] = 'RWrist'

# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm

bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
limb_length=[124,452,504,124,452,504,252,231,78,112,120,250,230,120,250,230]


data_f_3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
data_f_5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')  


frame=0

scene=canvas()
scene.camera.pos=vector(1,-2000,0)
scene.camera.axis=vector(-1,+2000,0)
scene.up=vector(0,0,1)
scene.userzoom =True
scene.userspin=True
scene.width = scene.height = 600
#scene.background= color.white
distant_light(direction=vector( 0.88,  -0.44,  0.2),       color=color.gray(0.8))
scene.title = "\n Pose Visualisation \n"   
scene.caption = """\n To rotate humanoid, drag with right button
To zoom, drag with middle button\n
Adjust slider to change frame: \n\n
"""

############################################################################

skeleton=[]
jeleton=[]

#skeleton1=[]
#jeleton1=[]


#make sure time matches for each (to be corrected by xcorr eventually)
plot1=data_f_3.iloc[:,37:139]
plot1.columns = range(plot1.shape[1])

plot2=data_f_5.iloc[:,25:127]
plot2.columns = range(plot2.shape[1])

if np.size(plot1,1)!=np.size(plot2,1):
    print
#for d lines
d_lines=[]

#plot axis
arx=arrow(pos=vector(500,0,0),axis=vector(100,0,0),color=vec(1,0,0))
ary=arrow(pos=vector(500,0,0),axis=vector(0,100,0),color=vec(0,1,0))
arz=arrow(pos=vector(500,0,0),axis=vector(0,0,100),color=vec(0,0,1))

#simulation initialisation

temp=sim(skeleton,jeleton,frame,plot1,bones,joints,limb_length,vec(0,1,0),True,False,vec(1,1,1))
skeleton=temp[0]
jeleton=temp[1]


start=plot1[frame]
end=plot2[frame]
delta=np.subtract(end[joints[-1]],start[joints[-1]])
start_temp=start[joints[-1]]






#    #joint angle colouring
#    angles1=ja.joint_angle(frame,plot1,bones,joints)  
#    angles2=ja.joint_angle(frame,plot2,bones,joints) 
#    angles=np.subtract(angles1,angles2)
#
#    red = Color("blue")
#    colors = list(red.range_to(Color("green"),70))
#    
#    for i in range(len(jeleton)):
#        if angles[i]==0:
#            jeleton[i].color=color.white
#        else:
#            rgbc=colors[abs(int(angles[i]))].rgb
#            jeleton[i].color=vector(rgbc[0],rgbc[1],rgbc[2])
#
#
#    
#    A.append(angles1[15])
#    B.append(angles2[15])    
   


##############################################################################

####################################################################
#scene.range = 1.8


running = True


#slider 
def fr(s):
    global running
    
    running = True
    wt.text='{:1}'.format(sl.value)

sl = slider(min=0, max=np.size(plot1,1)-1, value=1, length=500, step=1, bind=fr)

wt = wtext(text='1'.format(sl.value))
scene.append_to_caption(' frame \n <br>')
##############################################################
graph_type=0
def M(m):
    global graph_type
    
    val = m.selected
    
    if val == "TimeColour3D": 
        graph_type = 0
    elif val == "Hagerstrand": 
        graph_type = 1

menu(choices=['TimeColour3D', 'Hagerstrand'], index=0, bind=M)

###################################################
def Run(b):
    global index
    if index==None:
        warning.text="""  <font color="red"> No joint selected </font> """
    else:
        warning.text=""
        if val ==0:
            rngid= vis.TimeColour3D(plot1,index,bones,joints)
    #        scene.append_to_caption("<img src='me.jpg'/>")
            gwt.text="\n <img src='%f.jpg'/>"%rngid
        
        if val==1:
            

    
button(text="3D plot", pos=scene.caption_anchor, bind=Run)
scene.append_to_caption('<br>')
warning= wtext(text="\n",pos=scene.caption_anchor)

gwt = wtext(text="\n",pos=scene.caption_anchor)

lasthit = None
lastpick = None
lastcolor = None
index=None

def getevent():
    global lasthit, lastpick, lastcolor, index
    if lasthit != None:
        if lastpick != None: lasthit.modify(lastpick, color=lastcolor)
        else: lasthit.color = vector(lastcolor)
        lasthit = lastpick = None
    
    hit = scene.mouse.pick
    if hit != None:
        lasthit = hit
        lastpick = None
        lastcolor = vector(hit.color) # make a copy
        hit.color = color.red
    if hit in jeleton:
        print(jeleton.index(hit))
        index=jeleton.index(hit)
#    if hit in skeleton:
#        print(skeleton.index(hit))
#        index=skeleton.index(hit)
    else:
        print("not in list")

scene.bind("mousedown", getevent)


while True:
    if running:

        frame= sl.value    
        
        for i in range(len(bones)):
            start=plot1[frame][bones[i][0]]
            end=plot1[frame][bones[i][1]]
            delta=np.subtract(end,start)
            
            skeleton[i].pos=vector(start[0],start[1],start[2])
            skeleton[i].axis=vector(delta[0],delta[1],delta[2])
            
        for i in range(len(joints)):
            start=plot1[frame][joints[i]]
            jeleton[i].pos=vector(start[0],start[1],start[2])
        
        running = False
        
