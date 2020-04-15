# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 01:49:34 2020

@author: neilw
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from fastdtw import fastdtw
from scipy.spatial.distance import euclidean


from dtw_combined import smart_sel2
from dtw_combined import dtwrecon
from dtw_combined import dtwhighlight
from v1f import v1
from v2f import v2
from v3f import v3
from v8f import v8
from v9f import v9
from v10f import v10
from v4f import v4
from v11f import v11
from v15f import v15

top=[3,5,2]
bott=[1,10,8,9,4,6]

#dtwdlist=dtwrecon(top,v1(3))
#[chose_times,separation,rangel]=dtwhighlight(top,bott,dtwdlist)
#
#
##raw = 'asdfa3fa'
functions = [v1, v4, v15]
##choose joint using func(joint index)
isanything = [dtwhighlight(top,bott,dtwrecon(top,func(2))) for func in functions]

