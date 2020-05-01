# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 03:32:46 2020

@author: neilw
"""
from v1f import v1
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np

x=v1(13)
s1 = x.iloc[2]
s2 = x.iloc[7]
d, paths = dtw.warping_paths(s1, s2, window=200, psi=2)
best_path = dtw.best_path(paths)
dtwvis.plot_warpingpaths(s1, s2, paths, best_path)