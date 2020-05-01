# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:47:19 2020

@author: neilw
"""

from sympy import *
def asCartesian(rthetaphi):
    #takes list rthetaphi (single coord)
    r       = rthetaphi[0]
    theta   = rthetaphi[1]* pi/180 # to radian
    phi     = rthetaphi[2]* pi/180
    x = r * sin( theta ) * cos( phi )
    y = r * sin( theta ) * sin( phi )
    z = r * cos( theta )
    return [x,y,z]

def asSpherical(xyz):
    #takes list xyz (single coord)
    x       = xyz[0]
    y       = xyz[1]
    z       = xyz[2]
    r       =  sqrt(x*x + y*y + z*z)
    theta   =  acos(z/r)*180/ pi #to degrees
    phi     =  atan2(y,x)*180/ pi
    return [r,theta,phi]