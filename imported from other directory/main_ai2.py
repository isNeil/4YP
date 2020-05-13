# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:17:09 2020

@author: neilw
"""

from vpython import *
import pandas as pd
import numpy as np
from sim import create_frame
from sim import frame_init
import vis2 as vis
from smart_frame_select import smart_sel
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

plot3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\3.json')
plot4= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\4.json')
plot5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\5.json')
plot6= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\6.json')
plot7= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\7.json')
plot8= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\8.json')
plot9= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\9.json')
plot10= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\102\10.json')

plot1=plot4
plot2=plot3

#data_f_3= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF3formated.json')
#data_f_5= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\jsondata\RF5formated.json')  
#
##chooes frames to match length for each (to be corrected by xcorr eventually)
#plot1=data_f_3.iloc[:,41:143]
#plot1.columns = range(plot1.shape[1])
#
#plot2=data_f_5.iloc[:,28:130]
#plot2.columns = range(plot2.shape[1])

#-----------------------------------------------------------------------------
#scene settings

scene=canvas()
scene.camera.pos=vector(1,-2000,0)
scene.camera.axis=vector(-1,+2000,0)
scene.up=vector(0,0,1)
scene.userzoom =True
scene.userspin=True
scene.width = 600
scene.height = 900
#scene.background= color.white
scene.align="right"
distant_light(direction=vector(0.88,-0.44,0.2),color=color.gray(0.8))

#-----------------------------------------------------------------------------
#scene title and captions

  
scene.caption = """<b>Pose Visualisation</b>\n
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
#------------------------------------------------------------------------------
#change plot menu
plot_num= 1
def M2(m):
    global plot_num,plot1,plot3,plot4,plot5,plot6,plot7,plot8,plot9,plot10,running
    val = m.selected
    if val == "Plot 4": 
        plot1= plot4
        plot_num = 1
        gwt2.text="\n\n<img src='std_vis_1.jpg'/>"
    elif val == "Plot 5":
        plot1=plot5
        plot_num = 2
        gwt2.text="\n\n<img src='std_vis_2.jpg'/>"
    elif val == "Plot 6":
        plot1=plot6
        plot_num = 3
        gwt2.text="\n\n<img src='std_vis_3.jpg'/>"
    elif val == "Plot 7":
        plot1=plot7
        plot_num = 4
        gwt2.text="\n\n<img src='std_vis_4.jpg'/>"
    elif val == "Plot 8":
        plot1=plot8
        plot_num = 5
        gwt2.text="\n\n<img src='std_vis_5.jpg'/>"
    elif val == "Plot 9":
        plot1=plot9
        plot_num = 6
        gwt2.text="\n\n<img src='std_vis_6.jpg'/>"
    elif val == "Plot 10":
        plot1=plot10
        plot_num = 7
        gwt2.text="\n\n<img src='std_vis_7.jpg'/>"
    elif val == "Plot 3":
        plot1 = plot3
        plot_num =0
        gwt2.text="\n\n<img src='std_vis_0.jpg'/>"
    running =True
plot_menu=menu(choices=['Plot 3','Plot 4','Plot 5','Plot 6','Plot 7','Plot 8','Plot 9','Plot 10'], index=1, bind=M2)
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

show_b=button(text="Hide comparison", pos=scene.caption_anchor, bind=Show)


#----------------------------------------------------------------------------
#smart plot 

#gwt2 = wtext(text="\n\n<img src='std_pos_vis_%d_%d.jpg'/>"%(j_index,plot_num),pos=scene.caption_anchor)
gwt2 = wtext(text="\n\n<img src='std_vis_1.jpg'/>",pos=scene.caption_anchor)

#-----------------------------------------------------------------------------
scene.append_to_caption( "\n\n Adjust slider to change frame of animation: \n\n")


anime= True
def Play(b):
    global anime
    if anime== True:
        anime = False
        b.text="Play"
        
    else:
        anime = True
        b.text="Pause"
        

play_b=button(text="Pause", pos=scene.caption_anchor, bind=Play)

var_speed= True
def Timewarp(b):
    global var_speed
    if var_speed== True:
        var_speed = False
        b.text="Timewarp On"
        
    else:
        var_speed = True
        b.text="Timewarp Off"
        

time_b=button(text="Timewarp Off", pos=scene.caption_anchor, bind=Timewarp)

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
    elif val == "TC3DLimb":
        graph_type = 2
    elif val == "StdPos":
        graph_type = 3
graph_menu=menu(choices=['TimeColour3D', 'Hagerstrand','TC3DLimb','StdPos'], index=0, bind=M)


#-----------------------------------------------------------------------------
#Plot graphs button
graph_id=0
j_index=None
s_index=None
def Run(b):
    global j_index,graph_type,graph_id,s_index
    if j_index==None and s_index==None:
        
        warning.text="""  <font color="red"> No joint or bone selected </font> """
    else:
        warning.text=""
        if graph_type ==0:
            if j_index!=None and s_index==None:
                warning.text="""  <font color="red"> Loading graph </font> """
                vis.TimeColour3DJ(plot1,j_index,bones,joints,graph_id)
                gwt.text="\n\n3D position of each frame plotted. Colour scale from blue to green varies with time:\n\n <img src='graph%d.jpg'/>"%graph_id
                warning.text=""
                # gwt2.text="\n"
            elif j_index==None and s_index!=None:
                warning.text="""  <font color="red"> Loading graph </font> """
                vis.TimeColour3DS(plot1,s_index,bones,joints,graph_id)
                gwt.text="\n\n3D position of each frame plotted. Colour scale from blue to green varies with time:\n\n <img src='graph%d.jpg'/>"%graph_id
                warning.text=""
#            else:
#                warning.text="""  <font color="red"> Both joint and bone selected</font> """
                #considering requiring multiple to be selected
        elif graph_type ==1:
            if s_index!=None:
                warning.text="""  <font color="red"> Select a joint</font> """
            else:
                warning.text="""  <font color="red"> Loading graph </font> """
                vis.Hagerstrand(plot1,j_index,bones,joints,graph_id)
                gwt.text="\n\n1st figure shows position in y-z plane with time in x direction. 2nd figure shows position in x-y plane with time in y direction:\n\n <img src='graph%d.jpg'/>"%graph_id
                warning.text=""
                #gwt2.text="\n <img src='%f.jpg'/>"%rngid
        
        elif graph_type ==2:
            if j_index!=None:
                if j_index-1<0 or j_index+1>=len(joints):
                    warning.text="""  <font color="red"> Select a limb joint! (elbows and knees only)</font> """
                elif joints[j_index-1]+1!=joints[j_index+1]-1:
                    warning.text="""  <font color="red"> Select a limb joint! (elbows and knees only)</font> """
                    
                else:
                    warning.text="""  <font color="red"> Loading graph </font> """
                    vis.TC3DLimb(plot1,j_index,bones,joints,graph_id)
                    gwt.text="\n\n3D position of each frame plotted. Colour scale from blue to green varies with time:\n\n <img src='graph%d.jpg'/>"%graph_id
                    warning.text=""
            else: 
                warning.text="""  <font color="red"> Select a limb joint</font> """
        elif graph_type ==3:
            if j_index!=None and s_index==None:
                warning.text="""  <font color="red"> Loading graph </font> """
                #for current plots week 6 all premade for joint 16
            
                vis.plotpositionalderivatives(j_index,bones,joints,plot_num)
                gwt.text="\n\nStandard selection of visualisations for a joint:\n\n <img src='std_pos_vis_%d_%d.jpg'/>"%(j_index,plot_num)
                warning.text=""
                # gwt2.text="\n"
            else:
                warning.text="""  <font color="red"> Select a joint </font> """
            
            
        graph_id+=1
        
run_b=button(text="3D plot", pos=scene.caption_anchor, bind=Run)
#scene.append_to_caption('<br>')
warning= wtext(text="\n",pos=scene.caption_anchor)

#--------------------------------------------------------------------------
#dynamic text for graph plots
gwt = wtext(text="\n",pos=scene.caption_anchor)


#----------------------------------------------------------------------------
#select joint 

lasthit = None
lastpick = None
lastcolor = None

def getevent():
    global lasthit, lastpick, lastcolor, j_index,s_index
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
        s_index=None
        print("joint selected")
    elif hit in skeleton:
        s_index=skeleton.index(hit)
        j_index=None
        print("bone selected")
        print(s_index)
    else:
        print("not in list")
        j_index=None
        s_index=None

scene.bind("mousedown", getevent)
#-----------------------------------------------------------------------------
#update frames when running = True
hl=smart_sel()


while True:
    
    
    if anime:
        if var_speed:
            if frame in hl[plot_num]:        
                sleep(1/2)

    
        sleep(1/14)
        sl.value=frame    
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
        wt.text='{:1}'.format(sl.value)
        if frame<np.size(plot1,1)-1:   
            frame +=1
        else:
            frame =0
       
            
    elif running:
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
        
