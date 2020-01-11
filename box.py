# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:49:36 2020

@author: neilw
"""

from vpython import *


scene=canvas()
scene.camera.pos=vector(0,-10,0)
scene.camera.axis=vector(0,+10,0)
scene.up=vector(1,-1,0)
scene.userzoom =False
scene.userspin=True
scene.width = scene.height = 1000
box()