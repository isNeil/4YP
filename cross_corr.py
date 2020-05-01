# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 03:10:14 2020

@author: neilw
"""
#####################
#stupid idea  to try to cross correlate in 4d way too much computation
#####################
import pandas as pd
import numpy as np
from formatdata import format
from collections import Counter
from scipy import signal
from simulation import sim
import matplotlib.pyplot as plt
import tensorflow as tf
import random

random.seed(1)
x=np.random.rand(5,3,3)

filters=np.array([[[0.16660719, 0.00501336, 0.81967298],[0.35217891, 0.46993   , 0.0840033 ],[0.69931119, 0.76569761, 0.27203308]],[[0.26616616, 0.14368727, 0.129982  ],[0.44728883, 0.56462922, 0.09881968],[0.90546202, 0.96769744, 0.54353342]],[[0.37580248, 0.97301764, 0.00161488], [0.40937852, 0.510239  , 0.41020811], [0.1320832 , 0.46001288, 0.09261623]]])

convolution=tf.nn.conv3d(x,filters,strides=[1, 1, 1, 1,1],padding='SAME')

def lag_finder(y1, y2, sr):
    n = len(y1)

    corr = signal.correlate(y2, y1, mode='same') / np.sqrt(signal.correlate(y1, y1, mode='same')[int(n/2)] * signal.correlate(y2, y2, mode='same')[int(n/2)])

    delay_arr = np.linspace(-0.5*n/sr, 0.5*n/sr, n)
    delay = delay_arr[np.argmax(corr)]
    print('y2 is ' + str(delay) + ' behind y1')

    plt.figure()
    plt.plot(delay_arr, corr)
    plt.title('Lag: ' + str(np.round(delay, 3)) + ' s')
    plt.xlabel('Lag')
    plt.ylabel('Correlation coeff')
    plt.show()


#lag_finder(data_f_new[:][31],data_f_new_3[:][31],100)

