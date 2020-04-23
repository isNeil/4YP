# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:22:35 2020

@author: neilw
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colour import Color
from extractframes import extractframes
from v1f import v1
from v2f import v2
from v3f import v3
from v5f import v5
from v6f import v6
from v8f import v8
from v9f import v9
from v10f import v10
from v4f import v4
from v11f import v11
from v15f import v15
from v16f import v16
from v17f import v17
from v18f import v18
from dtw_combined2 import dtwd
from dtw_combined2 import dtwrecon
from dtw_combined2 import smart_sel2
from warpvisualisation import dtwdnew
import pickle
import matplotlib
from matplotlib import cm
#plot1= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3.json')
#plot2= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5.json')
#plot1vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3vel.json')
#plot2vel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5vel.json')
#plot1accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot1rf3accel.json')
#plot2accel= pd.read_json(r'C:\Users\neilw\Desktop\RF Vpython\RFVP\json\plot2rf5accel.json')

#    #index mapping
#    bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
#    joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
    

def TimeColour3DJ(plot1,index,bones,joints,graph_id):
 
    frames=np.shape(plot1)[1]
    #joint 0 to 27 Rwrist
    plot1x=[]
    plot1y=[]
    plot1z=[]
    #mapping index to joint 
    dex=joints[index]
    
    for i in range(np.shape(plot1)[1]):
        plot1x.append(plot1.iloc[dex][i][0])
        plot1y.append(plot1.iloc[dex][i][1])
        plot1z.append(plot1.iloc[dex][i][2])
                                      
    fig = plt.figure(figsize=(12.5, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    red = Color("blue")
    colors = list(red.range_to(Color("green"),102))
    
    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)
    
    #make axis fit correctly
    xm=(max(plot1x)+min(plot1x))/2
    ym=(max(plot1y)+min(plot1y))/2
    zm=(max(plot1z)+min(plot1z))/2
    
    ax.scatter(plot1x, plot1y, plot1z, zdir='z', depthshade=True,alpha=0.9,c=rgbc)
    ax.scatter(plot1x, plot1y, [zm-600]*frames, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    ax.scatter([xm-600]*frames, plot1y, plot1z, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    ax.scatter(plot1x, [ym+600]*frames,  plot1z, zdir='z',alpha=0.2,c=rgbc) #cmap=cm.coolwarm)
    
    ax.set_xlabel('X')
    ax.set_xlim(xm-600, xm+600)
    ax.set_ylabel('Y')
    ax.set_ylim(ym-600, ym+600)
    ax.set_zlabel('Z')
    ax.set_zlim(zm-600, zm+600)
    plt.tight_layout()

    plt.savefig("Images/graph%d.jpg"%graph_id, dpi=60)  
    
    plt.show()
    
    
def TimeColour3DS(plot1,index,bones,joints,graph_id):

    frames=np.shape(plot1)[1]
    #joint 0 to 27 Rwrist
    plot1x=[]
    plot1y=[]
    plot1z=[]
    x=[]
    y=[]
    z=[]
    #mapping index to bones to find joint number
    dex=bones[index][0]
    dex_prev=bones[index][1]
    
    for i in range(np.shape(plot1)[1]):
        plot1x.append(plot1.iloc[dex][i][0])
        plot1y.append(plot1.iloc[dex][i][1])
        plot1z.append(plot1.iloc[dex][i][2])
        x.append(plot1.iloc[dex_prev][i][0])
        y.append(plot1.iloc[dex_prev][i][1])
        z.append(plot1.iloc[dex_prev][i][2])
                                  
    fig = plt.figure(figsize=(12.5, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    red = Color("blue")
    colors = list(red.range_to(Color("green"),len(plot1)))
    
    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)

    #make axis fit correctly
    xm=(max(plot1x)+min(plot1x))/2
    ym=(max(plot1y)+min(plot1y))/2
    zm=(max(plot1z)+min(plot1z))/2
    

    for i in range(frames):
        ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[plot1z[i],z[i]], color=rgbc[i])
        ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[zm-600,zm-600],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([xm-600,xm-600], [plot1y[i],y[i]], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([plot1x[i],x[i]], [ym+600,ym+600], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)

    ax.set_xlabel('X')
    ax.set_xlim(xm-600, xm+600)
    ax.set_ylabel('Y')
    ax.set_ylim(ym-600, ym+600)
    ax.set_zlabel('Z')
    ax.set_zlim(zm-600, zm+600)
    plt.tight_layout()

    plt.savefig("Images/graph%d.jpg"%graph_id, dpi=60)  

    plt.show()

def TC3DLimb(plot1,index,bones,joints,graph_id):
    #take joint in between bones
    
    frames=np.shape(plot1)[1]
    #mapping index to bones to find joint number
    
    
    
    dex=joints[index]
    dex_prev=joints[index-1]
    dex_post=joints[index+1]
    #check it actually is a limb joint by saying limbs are sequential numbers- bit of a gimmicky method- MOVED INTO menu 
    
    print(dex)
    print(dex_prev)
    print(dex_post)
    
    plot1x=[]
    plot1y=[]
    plot1z=[]
    x=[]
    y=[]
    z=[]
    x1=[]
    y1=[]
    z1=[]
    
    for i in range(np.shape(plot1)[1]):
        plot1x.append(plot1.iloc[dex_post][i][0])
        plot1y.append(plot1.iloc[dex_post][i][1])
        plot1z.append(plot1.iloc[dex_post][i][2])
        x.append(plot1.iloc[dex][i][0])
        y.append(plot1.iloc[dex][i][1])
        z.append(plot1.iloc[dex][i][2])
        x1.append(plot1.iloc[dex_prev][i][0])
        y1.append(plot1.iloc[dex_prev][i][1])
        z1.append(plot1.iloc[dex_prev][i][2])                  
                      
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    #ax.view_init(20, 200)
    red = Color("blue")
    colors = list(red.range_to(Color("green"),len(plot1)))
    
    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)
        
    #make axis fit correctly
    xm=(max(x)+min(x))/2
    ym=(max(y)+min(y))/2
    zm=(max(z)+min(z))/2
    
    for i in range(frames):
        
        ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[plot1z[i],z[i]], color=rgbc[i])
        ax.plot([plot1x[i],x[i]],[plot1y[i],y[i]],[zm-600,zm-600],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([xm-600,xm-600], [plot1y[i],y[i]], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([plot1x[i],x[i]], [ym+600,ym+600], [plot1z[i],z[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        
        ax.plot([x[i],x1[i]],[y[i],y1[i]],[z[i],z1[i]], color=rgbc[i])
        ax.plot([x[i],x1[i]],[y[i],y1[i]],[zm-600,zm-600],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([xm-600,xm-600], [y[i],y1[i]], [z[i],z1[i]],color=rgbc[i],alpha=0.2) #cmap=cm.coolwarm)
        ax.plot([x[i],x1[i]], [ym+600,ym+600], [z[i],z1[i]],color=rgbc[i],alpha=0.2) #cmap=cm.c
   
    ax.set_xlabel('X')
    ax.set_xlim(-700, 700)
    ax.set_ylabel('Y')
    ax.set_ylim(-700, 700)
    ax.set_zlabel('Z')
    ax.set_zlim(-400, 1000)   
    
    plt.tight_layout()
    plt.savefig("Images/graph%d.jpg"%graph_id, dpi=60)    
    
    plt.show()
    
def Hagerstrand(plot1,index,bones,joints,graph_id):
    
    frames=np.shape(plot1)[1]
    #joint 0 to 27 Rwrist   
    plot1x=[]
    plot1y=[]
    plot1z=[]    
    #mapping index to joint 
    dex=joints[index]   
    for i in range(np.shape(plot1)[1]):
        plot1x.append(plot1.iloc[dex][i][0])
        plot1y.append(plot1.iloc[dex][i][1])
        plot1z.append(plot1.iloc[dex][i][2])
                                           
    fig = plt.figure(figsize=(25, 10))
    ax = fig.add_subplot(121, projection='3d')
    
    red = Color("blue")
    colors = list(red.range_to(Color("green"),len(plot1)))

    rgbc=[]
    for i in colors:
        rgbc.append(i.rgb)
    
    ax.scatter((list(range(frames))), plot1y, plot1z, zdir='z', depthshade=True,alpha=0.9,c=rgbc)
    
    #make axis fit correctly
    xm=(max(plot1x)+min(plot1x))/2
    ym=(max(plot1y)+min(plot1y))/2
    zm=(max(plot1z)+min(plot1z))/2
    
    ax.scatter((list(range(frames))), plot1y, [zm-600]*frames, zdir='z',alpha=0.2,c=rgbc) #z)
    ax.scatter(-10, plot1y, plot1z, zdir='z',alpha=0.2,c=rgbc) #x)
    ax.scatter((list(range(frames))), [ym+600]*frames,  plot1z, zdir='z',alpha=0.2,c=rgbc) #y)
    
    ax.set_xlabel('X')
    ax.set_xlim(-10, frames+10)
    ax.set_ylabel('Y')
    ax.set_ylim(ym-600, ym+600)
    ax.set_zlabel('Z')
    ax.set_zlim(zm-600, zm+600)

    ######################################
    
    ax1= fig.add_subplot(122, projection='3d')
    ax1.scatter(plot1x, plot1y, (list(range(frames))), zdir='z', depthshade=True,alpha=0.9,c=rgbc)
    
    ax1.scatter([xm-600]*frames, plot1y, (list(range(frames))), zdir='z',alpha=0.2,c=rgbc) #x)
    ax1.scatter(plot1x, [ym+600]*frames,(list(range(frames))), zdir='z',alpha=0.2,c=rgbc) #y)
    ax1.scatter(plot1x, plot1y, -10, zdir='z',alpha=0.2,c=rgbc) #z
    
    ax1.set_xlabel('X')
    ax1.set_xlim(xm-600, xm+600)
    ax1.set_ylabel('Y')
    ax1.set_ylim(ym-600, ym+600)
    ax1.set_zlabel('Z')
    ax1.set_zlim(-10, frames+10)
        

    plt.tight_layout()
    plt.savefig("Images/graph%d.jpg"%graph_id, dpi=60)    
    
    plt.show()
        
def plotpositionalderivatives(index,bones,joints,plot_num):
    #plot number starts from 0 i.e. plot 0  is for rf3
    top=[3,5,2]
  
    hl= extractframes(v1(3),plot_num)
    
    
    fig, axs = plt.subplots(4,2,figsize=(13, 5))
    axs[0,0].title.set_text('Mean Separation')
    axs[1,0].title.set_text('Variance Sepearation')
    axs[2,0].title.set_text('DTW w.r.t. comparison.')
    axs[3,0].title.set_text('DTW w.r.t. reference')
    axs[0,1].title.set_text('DTW w.r.t reference')
    axs[1,1].title.set_text('DTW w.r.t reference')
    axs[2,1].title.set_text('DTW w.r.t reference')
    axs[3,1].title.set_text('DTW w.r.t reference')
    
    for i in hl:
#        axs[0,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
#        axs[1,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
#        axs[2,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[3,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)

        axs[0,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[1,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[2,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        axs[3,1].axvspan(i, i+1, facecolor='grey', alpha=0.3)
        
    path=smart_sel2(v1(index),top[0]-1,plot_num)
    new_hl=[]
    for i in path:
        if i[1] in hl:
              new_hl.append(i[0])  
    for i in new_hl:
        axs[2,0].axvspan(i, i+1, facecolor='grey', alpha=0.3)
                 
              
    df=v1(index)
    axs[0,0].plot(df.iloc[0,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[1,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[2,:],'r')
    axs[0,0].plot(df.iloc[3,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[4,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[5,:],'b',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[0,0].plot(df.iloc[7,:],'b',alpha=0.3) 
    axs[0,0].plot(df.iloc[plot_num,:],'black')
    axs[0,0].set_ylabel('Distance')
   # axs[0,0].set_xlabel('Frame')   



    dfata=dtwdnew(v1(index),2,plot_num)
#    axs[1,0].bar(range(len(dfata)),dfata)
    axs[1,0].plot(dfata)
    for i in range(len(dfata)):
        if dfata[i]>1:
            axs[2,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
        elif dfata[i]<1:
            axs[2,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
            
    
    
    axs[1,0].set_ylabel('Relative Rate')
  #  axs[1,0].set_xlabel('Frame')   
    
        
    dfata=dtwdnew(v1(index),plot_num,2)
    for i in range(len(dfata)):
        if dfata[i]>1:
            axs[3,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
        elif dfata[i]<1:
            axs[3,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
    dfataref=np.zeros(len(path))
    for i in path:
        dfataref[i[0]]=dfata[i[1]]
    for i in range(len(dfataref)):
        if dfataref[i]>1:
            axs[3,0].axvspan(i, i+1, facecolor='blue', alpha=0.2)
        elif dfataref[i]<1:
            axs[3,0].axvspan(i, i+1, facecolor='orange', alpha=0.2)
    
    df=dtwrecon([plot_num+1],v1(index))
    axs[2,0].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[1,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[2,:],'r')
    axs[2,0].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[4,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[0,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[2,0].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[2,0].plot(df.iloc[plot_num,:],'black')
    axs[2,0].set_ylabel('Distance')
  #  axs[2,0].set_xlabel('Frame')

    df=dtwrecon(top,v1(index))
    axs[3,0].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[1,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[2,:],'r')
    axs[3,0].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[4,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[0,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[3,0].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[3,0].plot(df.iloc[plot_num,:],'black')
    axs[3,0].set_ylabel('Distance')
    axs[3,0].set_xlabel('Frame')

    
    df=dtwrecon(top,v16(index))
    axs[0,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[1,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[2,:],'r')
    axs[0,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[4,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[0,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[0,1].plot(df.iloc[7,:],'g',alpha=0.3)
    axs[0,1].plot(df.iloc[plot_num,:],'black')
    axs[0,1].set_ylabel('Displacement X')
 #   axs[0,1].set_xlabel('Frame')    
    #normalise
  
        
    df=dtwrecon(top,v17(index))
    axs[1,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[1,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[2,:],'r')
    axs[1,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[4,:],'g',alpha=0.3)
    axs[1,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[2,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[1,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[1,1].plot(df.iloc[plot_num,:],'black')
    axs[1,1].set_ylabel('Displacement Y')
  #  axs[1,1].set_xlabel('Frame')
    #normalise


    df=dtwrecon(top,v18(index))
    axs[2,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[1,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[2,:],'r')
    axs[2,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[4,:],'g',alpha=0.3)
    axs[2,1].plot(df.iloc[5,:],'g',alpha=0.3)
    #axs[2,1].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[2,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[2,1].plot(df.iloc[plot_num,:],'black')
    axs[2,1].set_ylabel('Displacement Z')
   # axs[2,1].set_xlabel('Frame')   

 
    df=dtwrecon(top,v4(index))
    axs[3,1].plot(df.iloc[0,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[1,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[2,:],'r')
    axs[3,1].plot(df.iloc[3,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[4,:],'g',alpha=0.3)
    axs[3,1].plot(df.iloc[5,:],'g',alpha=0.3)
   # axs[3,0].plot(df.iloc[6,:],'b',alpha=0.3)
    axs[3,1].plot(df.iloc[7,:],'g',alpha=0.3)   
    axs[3,1].plot(df.iloc[plot_num,:],'black')
    axs[3,1].set_ylabel('Angle')
    axs[3,1].set_xlabel('Frame')
    #normalise

   

    
    #################################
#    functions = [v1,v2,v3,v4,v5,v6,v16,v17,v18]
#    output_mean,output_var = pickle.load(open("output.p","rb"))
#    a_mean = np.array(output_mean)
#    a_var = np.array(output_var)
#    ind_mean = np.argpartition(a_mean, -5)[-5:]
#    ind_var= np.argpartition(a_var,-5)[-5:]
#    a_mean[ind_mean]
#    a_var[ind_var]
#    
#    output_mean_formatted=[]
#    eachmeasure=[]
#    for j in range(len(functions)):
#        for i in range(17):
#            eachmeasure.append(output_mean[i+j*17])
#            
#        output_mean_formatted.append(eachmeasure)  
#        eachmeasure=[]
#    
#    print(output_mean_formatted)  
#    df = pd.DataFrame(output_mean_formatted) 
#    
#    df=df[[0,1,4,2,5,3,6,7,8,9,10,14,11,15,12,16,13]]
#    output_mean_formatted=df.values.tolist()
#    plt.figure(0)
#    viridis = cm.get_cmap('binary', 256)
#    newcolors = viridis(np.linspace(0, 1, 256))
#    
#    cmap = matplotlib.colors.ListedColormap(newcolors, name='colors', N=None)
#    
#    img = axs[4,1].imshow(output_mean_formatted, cmap=cmap)
#    
#    
#    x_label_list = ['Pelvis', 'R. Hip', 'L. Hip', 'R. Knee', 'L. Knee', 'R. Foot', 'L. Foot', 'Spine', 'Thorax', 'Neck', 'Head', 'R. Arm', 'L. Arm', 'R. Elbow', 'L. Elbow', 'R. Wrist', 'L. Wrist']
#    
#    axs[4,1].set_xticks(range(17))
#    
#    axs[4,1].set_xticklabels(x_label_list)
#    y_label_list = ['Distance', 'Speed', 'Acceleration', 'Angle', 'Angular Velocity', 'Angular Acceleration', 'X axis Displacement', 'Y axis Displacement','Z axis Displacement' ]
#    
#    axs[4,1].set_yticks(range(len(functions)))
#    
#    axs[4,1].set_yticklabels(y_label_list)
#    
    



    fig.tight_layout()

#    for preload
#    plt.savefig("Images/UI2/stdvis_trial_%d_keypoint_%d.jpg"%(plot_num,index), dpi=100)    


#bones=[[0,1],[1,2],[2,3],[0,6],[6,7],[7,8],[0,12],[12,13],[13,14],[14,15],[13,17],[17,18],[18,19],[13,25],[25,26],[26,27]]
#joints=[0,1,2,3,6,7,8,12,13,14,15,17,18,19,25,26,27]
#for i in range(10): 
#    for j in range(1,17):
#    
#        plotpositionalderivatives(16,bones,joints,i)
#        plt.close()
#plotpositionalderivatives(16,bones,joints,1)