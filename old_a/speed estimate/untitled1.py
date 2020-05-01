# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:08:44 2020

@author: neilw
"""

import cv2
import numpy as np

fxpx =1.1945e04
fypx =1.1902e04
cx=3.1195e03
cy =2.0635e03
cameramatrix = np.array([[fxpx,0,cx],
                         [0,fypx,cy],
                         [0,0,1]],dtype=np.float32)
objpoints = np.array([[50, 40,0],[50, 165,0],[100, 262,0],[110, 342,0],[165,120,0],[230,232,0],[302,70,0],[302,357,0],[352,190,0]], dtype=np.float32)
imagepoints = np.array([[622+1080, 4127-(2326+646)], [599+1080,4127-(1523+646) ], [1052+1080, 4127-(963+646)],[1093+1080, 4127-(571+646)],[1795+1080,4126-(1678+646)],[2304+1080,4127-(999+646)],[3285+1080,4127-(1843+646)],[2770+1080,4127-(343+646)],[3516+1080,4127-(1090+646)]], dtype=np.float32)

#left hand coordinate system
unkownvalue,rvec, tvec, inliers = cv2.solvePnPRansac(objpoints, imagepoints, cameramatrix ,np.zeros((5,1)),np.zeros((3,1)),np.zeros((3,1)))
rmat, _ = cv2.Rodrigues(rvec)

print("The world coordinate system's origin in camera's coordinate system:")
print("===camera rvec:")
print(rvec)
print("===camera rmat:")
print(rmat)
print("===camera tvec:")
print(tvec)
#print("ir_camera_shape: ")
#print(img.shape)

print("The camera origin in world coordinate system:")
print("===camera rmat:")
print(rmat.T)
print("===camera tvec:")
# the translation of camera in world coords is the negative of the rotated translation
print(-np.dot(rmat.T, tvec))

#retval, rvec, tvec = cv2.solvePnP(objpoints,imagepoints, cameramatrix, np.zeros(5))
#print('retval')
#print(retval)
#print('rvec')
#print(rvec)
#print('tvec')
#print(tvec)
print('pointcc')
pointwc=np.array([50,40,0])

pointcc=np.matmul(rmat,pointwc.T)#+tvec
print(pointcc)