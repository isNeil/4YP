# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:40:20 2019

@author: neilw
"""
import cv2
import numpy as np

fxpx =1.1945e04*1.2
fypx =1.1902e04*1.2
cx=1920/2
cy =1080/2
cameramatrix = np.array([[fxpx,0,cx],
                         [0,fypx,cy],
                         [0,0,1]],dtype=np.float32)
objpoints = np.array([[0, 0,0],[4.115, 0,0],[5.487, 0,0],[4.115,7,0],[0,7,0]], dtype=np.float32) #'''[5.487,7,0],'''
imagepoints = np.array([[99.043,1080-883.63], [1341.7,1080-938.89], [1827.9, 1080-968.4488],[2057, 787],[1041,749]], dtype=np.float32) #'''[2459,802],'''

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
pointwc=np.array([0,7,0])

pointcc=np.matmul(rmat,pointwc.T)#+tvec
print(pointcc)