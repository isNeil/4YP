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
from sim import create_frame
from sim import frame_init
import vis
#import calc_vel_accel as deltas
#import joint_angle as ja
#from spherical import asSpherical
#from spherical import asCartesian
#---------------------------------------------------------------------------- 
#Hard code joint order info

#    [0]  = 'Hip'   [1]  = 'RHip'   [2]  = 'RKnee'   [3]  = 'RFoot'   [6]  = 'LHip'   [7]  = 'LKnee'   [8]  = 'LFoot'   [12] = 'Spine'   [13] = 'Thorax'
#    [14] = 'Neck/Nose'   [15] = 'Head'   [17] = 'LShoulder'   [18] = 'LElbow'   [19] = 'LWrist'   [25] = 'RShoulder'   [26] = 'RElbow'   [27] = 'RWrist'

# 1.R pelvis [124] 2.R femur[452] 3.R tibia[504] 4.L pelvis[124] 5.L femur 6.L tibia 7.lowerback[252] 8.upperback[231] 9.neck[78] 10.head [112]
#11.L clavicle[120] 12.L upperarm[250] 13.L lowerarm[190] 14.R clav 15.R up arm 16.R low arm

bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]

#-----------------------------------------------------------------------------
#Load formatted data
data_f_3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
data_f_5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')  

#chooes frames to match length for each (to be corrected by xcorr eventually)
plot1=data_f_3.iloc[:,37:139]
plot1.columns = range(plot1.shape[1])

plot2=data_f_5.iloc[:,25:127]
plot2.columns = range(plot2.shape[1])

#-----------------------------------------------------------------------------
#scene settings

scene=canvas()
scene.camera.pos=vector(1,-2000,0)
scene.camera.axis=vector(-1,+2000,0)
scene.up=vector(0,0,1)
scene.userzoom =True
scene.userspin=True
scene.width = scene.height = 600
#scene.background= color.white
distant_light(direction=vector(0.88,-0.44,0.2),color=color.gray(0.8))

#-----------------------------------------------------------------------------
#scene title and captions

scene.title = "Pose Visualisation\n\nSelect joint and choose visualisation technique to plot\n <br>"   
scene.caption = """\nDrag with right button to rotate model
Use middle mouse to zoom\n
Adjust slider to change frame of animation: \n\n
"""
#-----------------------------------------------------------------------------
#plot axis
arx=arrow(pos=vector(500,0,0),axis=vector(100,0,0),color=vec(1,0,0))
ary=arrow(pos=vector(500,0,0),axis=vector(0,100,0),color=vec(0,1,0))
arz=arrow(pos=vector(500,0,0),axis=vector(0,0,100),color=vec(0,0,1))
#-----------------------------------------------------------------------------
#simulation initialisation of first frame
frame=0

skeleton=[]
jeleton=[]

skeleton2=[]
jeleton2=[]

temp=frame_init(skeleton,jeleton,frame,plot1,bones,joints,True,False,vec(1,1,1))
skeleton=temp[0]
jeleton=temp[1]

temp=frame_init(skeleton2,jeleton2,frame,plot2,bones,joints,True,False,vec(0.5,0.5,0.5))
skeleton2=temp[0]
jeleton2=temp[1]

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
#    A.append(angles1[15])
#    B.append(angles2[15])    
   
running = True
#-----------------------------------------------------------------------------
#frame slider 
def fr(s):
    global running
    running = True
    wt.text='{:1}'.format(sl.value)

sl = slider(min=0, max=np.size(plot1,1)-1, value=1, length=500, step=1, bind=fr)
#slider text
wt = wtext(text='1'.format(sl.value))
scene.append_to_caption(' frame \n <br>')
#-----------------------------------------------------------------------------
#graph menu
graph_type=0
def M(m):
    global graph_type
    val = m.selected
    if val == "TimeColour3D": 
        graph_type = 0
    elif val == "Hagerstrand": 
        graph_type = 1

menu(choices=['TimeColour3D', 'Hagerstrand'], index=0, bind=M)

#-----------------------------------------------------------------------------
#Toggle comparison model
Visible=True
def Show(b):
    global Visible,running
    if Visible== True:
        b.text="Show comparison"
        Visible= False
        running=True
    else:
        b.text="Hide comparison"
        Visible= True
        running=True

show_b=button(text="Hide comparison", pos=scene.title_anchor, bind=Show)
#-----------------------------------------------------------------------------
#Plot graphs button

def Run(b):
    global j_index,graph_type
    if j_index==None:
        warning.text="""  <font color="red"> No joint selected </font> """
    else:
        warning.text=""
        if graph_type ==0:
            rngid= vis.TimeColour3D(plot1,j_index,bones,joints)
            gwt.text="\n3D position of each frame plotted. Colour scale from blue to green varies with time:\n <img src='%f.jpg'/>"%rngid
           # gwt2.text="\n"
        elif graph_type ==1:
            rngid= vis.Hagerstrand(plot1,j_index,bones,joints)
            gwt.text="\n1st figure shows position in y-z plane with time in x direction. 2nd figure shows position in x-y plane with time in y direction:\n <img src='%f.jpg'/>"%rngid
            #gwt2.text="\n <img src='%f.jpg'/>"%rngid
   
run_b=button(text="3D plot", pos=scene.caption_anchor, bind=Run)
#scene.append_to_caption('<br>')
warning= wtext(text="\n",pos=scene.caption_anchor)

#--------------------------------------------------------------------------
#dynamic text for graph plots
gwt = wtext(text="\n",pos=scene.caption_anchor)
gwt2 = wtext(text="\n",pos=scene.caption_anchor)

#----------------------------------------------------------------------------
#select joint 

lasthit = None
lastpick = None
lastcolor = None
j_index=None

def getevent():
    global lasthit, lastpick, lastcolor, j_index
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
        j_index=jeleton.index(hit)
#    if hit in skeleton:
#        print(skeleton.index(hit))
#        index=skeleton.index(hit)
    else:
        print("not in list")

scene.bind("mousedown", getevent)
#-----------------------------------------------------------------------------
#update frames when running = True

while True:
    if running:
        frame= sl.value    
        temp=create_frame(skeleton,jeleton,frame,plot1,bones,joints,True,False)
        skeleton=temp[0]
        jeleton=temp[1]
        if Visible:
            temp=create_frame(skeleton2,jeleton2,frame,plot2,bones,joints,Visible,False)
            skeleton2=temp[0]
            jeleton2=temp[1]
        else:
            for i in range(len(bones)):
                skeleton2[i].pos=vector(0,0,0)
                skeleton2[i].axis=vector(0,0,0)
                skeleton2[i].visible= Visible
            for i in range(len(joints)):
                jeleton2[i].pos=vector(0,0,0)
                jeleton2[i].visible= Visible        
        running = False
        
