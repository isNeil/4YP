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
from sim import trace_init
#from sim import trace_move
import vis2 as vis
from smart_frame_select import smart_sel
import pickle
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
plotlist=[plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9,plot10]

#plota is comparison
#plotb is reference
plota=plot1
plotb=plot3



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

temp=frame_init(skeleton,jeleton,frame,plota,bones,joints,True,vec(1,1,1))
skeleton=temp[0].copy()
jeleton=temp[1].copy()

#colour selected keypoint measure red
jeleton[1].color=vec(1,0,0)

temp=frame_init(skeleton2,jeleton2,frame,plotb,bones,joints,True,vec(0.5,0.5,0.5))
skeleton2=temp[0].copy()
jeleton2=temp[1].copy()

#############################################################################
all_traces=[]
tracetemp=[]
for j in range(len(joints)):
#    
    tracejoint = trace_init(tracetemp,plota,joints,j)
    all_traces.append(tracejoint)
    tracetemp=[]
###############################################################################
running = True
#------------------------------------------------------------------------------
#change joint menu
plot_num= 1
keypoint=1
def M3(m1):
    global keypoint, jeleton
    val = m1.selected
    dex=['R Hip','R Knee','R Foot','L Hip','L Knee','L Foot','Spine','Thorax','Neck','Head','L Arm','L Elbow','L Wrist','R Arm','R Elbow','R Wrist'].index(val)
    keypoint=dex+1
    gwt2.text="<img src='Images/UIresize2/stdvis_trial_%d_keypoint_%d.jpg' height='520' width='1300'/>"%(plot_num,keypoint)
    
#    #update COLOUR
    for jele in jeleton:
        jele.color=vec(1,1,1)   
    jeleton[keypoint].color=vec(1,0,0)     
#joint_menu=menu(choices=['Keypoint 1','Keypoint 2','Keypoint 3','Keypoint 4','Keypoint 5','Keypoint 6','Keypoint 7','Keypoint 8','Keypoint 9','Keypoint 10','Keypoint 11','Keypoint 12','Keypoint 13','Keypoint 14','Keypoint 15','Keypoint 16'], index=0, bind=M3)
joint_menu=menu(choices=['R Hip','L Hip','R Knee','L Knee','R Foot','L Foot','Spine','Thorax','Neck','Head','R Arm','L Arm','R Elbow','L Elbow','R Wrist','L Wrist'], index=0, bind=M3)





#change trial menu

def M2(m):
    global plot_num,plotlist,running,keypoint,plota, all_traces
    val = m.selected
    dex=['Trial 1','Trial 2','Trial 3','Trial 4','Trial 5','Trial 6','Anomaly','Trial 8','Trial 9','Trial 10'].index(val)
    plota=plotlist[dex]
    plot_num=dex
    gwt2.text="<img src='Images/UIresize2/stdvis_trial_%d_keypoint_%d.jpg' height='520' width='1300'/>"%(plot_num,keypoint)
    
    
    

    

        
trial_menu=menu(choices=['Trial 1','Trial 2','Trial 3','Trial 4','Trial 5','Trial 6','Anomaly','Trial 8','Trial 9','Trial 10'], index=0, bind=M2)
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
##############################################################################

gwt3 = wtext(text="\n\n Plot keypoint trace:",pos=scene.caption_anchor)



def tracevis3(b):
    global all_traces,running
    if b.checked:
        for i in all_traces[3]:
            i.visible = True
        running=True
    else:
        for i in all_traces[3]:
            i.visible = False
        running=True
checkbox(bind=tracevis3, text='R Foot')


def tracevis2(b):
    global all_traces,running
    if b.checked:
        for i in all_traces[2]:
            i.visible = True
        running=True
    else:
        for i in all_traces[2]:
            i.visible = False
        running=True
checkbox(bind=tracevis2, text='R Knee')


def tracevis16(b):
    global all_traces,running
    if b.checked:
        for i in all_traces[16]:
            i.visible = True
        running=True
    else:
        for i in all_traces[16]:
            i.visible = False
        running=True
checkbox(bind=tracevis16, text='R Hand')

def tracevis6(b):
    global all_traces,running
    if b.checked:
        for i in all_traces[6]:
            i.visible = True
        running=True
    else:
        for i in all_traces[6]:
            i.visible = False
        running=True
checkbox(bind=tracevis6, text='L Foot')


def tracevis5(b):
    global all_traces,running
    if b.checked:
        for i in all_traces[5]:
            i.visible = True
        running=True
    else:
        for i in all_traces[5]:
            i.visible = False
        running=True
checkbox(bind=tracevis5, text='L Knee')


def tracevis13(b):
    global all_traces,running
    if b.checked:
        for i in all_traces[13]:
            i.visible = True
        running=True
    else:
        for i in all_traces[13]:
            i.visible = False
        running=True
checkbox(bind=tracevis13, text='L Hand')
#----------------------------------------------------------------------------
#smart plot 

#gwt2 = wtext(text="\n\n<img src='std_pos_vis_%d_%d.jpg'/>"%(j_index,plot_num),pos=scene.caption_anchor)
titlematrices= wtext(text="\n\n<img src= 'Images/UIresize2/titlematrices.jpg' /><br>")
gwt2 = wtext(text="<img src='Images/UIresize2/stdvis_trial_1_keypoint_1.jpg' height='520' width='1300'/>",pos=scene.caption_anchor)
#
#-----------------------------------------------------------------------------
#scene.append_to_caption( "\n\n Adjust slider to change frame of animation: \n\n")
scene.append_to_caption( "\n\n")

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
        b.text="Time HL On"
        
    else:
        var_speed = True
        b.text="Time HL Off"
        

time_b=button(text="Time HL Off", pos=scene.caption_anchor, bind=Timewarp)

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

#-----------------------------------------------------------------------------

#--------------------------------------------------------------------------
#dynamic text for graph plots
#wt2 = wtext(text="\n  <style> #overlay {  position: fixed;  display = block  width: 100%;  height: 100%;  top: 0;  left: 0;  right: 0;bottom: 0; background-color: rgba(0,0,0,0.5); z-index: 2;  cursor: pointer;}</style>")
#wt2 = wtext(text="$('<textarea>fuck <textarea/>').val('Click above.\n').appendTo(scene.caption_anchor).css('width', '1000px').css('height', '90px').css('font-family', 'sans-serif').css('font-size', '14px')")
#T= $('body').append('This is a test.<br>')
#T = $('<textarea/>').val('Click above.\n').appendTo(scene.caption_anchor).css('width', '250px').css('height', '90px').css('font-family', 'sans-serif').css('font-size', '14px')
#frameslider0= wtext(text='<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script><script>$(document).ready(function(){$("button").click(function(){$("#overlay1").animate({left: "535px"});});});</script><button>Start Animation</button><div id="overlay1"; style="background:#98bf21;height:442px;width:535px;  top: 378px;  left: 86px; position:absolute;opacity: 0.5;"></div>')
frameslider1= wtext(text='')
frameslider2= wtext(text='')
frameslider3= wtext(text='')
frameslider4= wtext(text='')
frameslider5= wtext(text='')
frameslider6= wtext(text='')
frameslider7= wtext(text='')
frameslider8= wtext(text='')
#wt2= wtext(text='1')
#display: none;
#<script>
#function on() {
#  document.getElementById("overlay").style.display = "block";
#}
#
#function off() {
#  document.getElementById("overlay").style.display = "none";
#}
#</script>",pos=scene.caption_anchor)


#----------------------------------------------------------------------------
#select joint 

lasthit = None
lastpick = None
lastcolor = None

def getevent():
    global j_index,s_index
    
    hit = scene.mouse.pick
   
    if hit in jeleton:
        j_index=jeleton.index(hit)
        s_index=None
        joint_menu.index=j_index-1
        M3(joint_menu)
        print("joint selected")
    elif hit in  skeleton:
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
#load pickle of extractframes 
hl = pickle.load(open("extractedframes.p","rb"))

#run animation
while True:
    ##################################################
    sliderpos=75+frame*3.9
    sliderpos2=723+frame*3.9


    frameslider1.text='<div id="overlay"; style="background:#ff0000;height:95px;width:2px;  top: 375px;  left: %dpx; position:absolute;opacity: 1;"></div>'%(sliderpos)
    frameslider2.text='<div id="overlay"; style="background:#ff0000;height:95px;width:2px;  top: 375px;  left: %dpx; position:absolute;opacity: 1;"></div>'%(sliderpos2)
    frameslider3.text='<div id="overlay"; style="background:#ff0000;height:95px;width:2px;  top: 500px;  left: %dpx; position:absolute;opacity: 1;"></div>'%(sliderpos)
    frameslider4.text='<div id="overlay"; style="background:#ff0000;height:95px;width:2px;  top: 500px;  left: %dpx; position:absolute;opacity: 1;"></div>'%(sliderpos2)
    frameslider5.text='<div id="overlay"; style="background:#ff0000;height:94px;width:2px;  top: 626px;  left: %dpx; position:absolute;opacity: 1;"></div>'%(sliderpos)
    frameslider6.text='<div id="overlay"; style="background:#ff0000;height:94px;width:2px;  top: 626px;  left: %dpx; position:absolute;opacity: 1;"></div>'%(sliderpos2)
    frameslider7.text='<div id="overlay"; style="background:#ff0000;height:95px;width:2px;  top: 750px;  left: %dpx; position:absolute;opacity: 1;"></div>'%(sliderpos)
    frameslider8.text='<div id="overlay"; style="background:#ff0000;height:95px;width:2px;  top: 750px;  left: %dpx; position:absolute;opacity: 1;"></div>'%(sliderpos2)
    
    #################################################
    if anime:
        if var_speed:
            if frame in hl[plot_num]:        
                sleep(1/2)

    
        sleep(1/14)
        sl.value=frame    
        temp=create_frame(skeleton,jeleton,frame,plota,bones,joints,True)
        skeleton=temp[0]
        jeleton=temp[1]  
        if Visible:
            temp=create_frame(skeleton2,jeleton2,frame,plotb,bones,joints,Visible)
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
        #load frames for when not running but settings changed
        frame= sl.value    
        temp=create_frame(skeleton,jeleton,frame,plota,bones,joints,True)
        skeleton=temp[0]
        jeleton=temp[1]
        if Visible:
            temp=create_frame(skeleton2,jeleton2,frame,plotb,bones,joints,Visible)
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
        
