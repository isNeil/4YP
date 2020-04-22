# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:11:15 2020

@author: neilw
"""

import matplotlib.pyplot as plt
from v4f import v4

df=v4(2)
x=df.iloc[:][30]

plt.plot(0,x[0],'go')
plt.plot(0,x[1],'bo')
plt.plot(0,x[2],'bo')
plt.plot(0,x[3],'go')
plt.plot(0,x[4],'bo')
plt.plot(0,x[5],'go')
plt.plot(0,x[7],'go')
plt.plot(0,x[8],'go')
plt.plot(0,x[9],'go')

plt.savefig("Images/slice30.jpg", dpi=200) 
plt.close()

x=df.iloc[:][60]
plt.plot(0,x[0],'go')
plt.plot(0,x[1],'bo')
plt.plot(0,x[2],'bo')
plt.plot(0,x[3],'go')
plt.plot(0,x[4],'bo')
plt.plot(0,x[5],'go')
plt.plot(0,x[7],'go')
plt.plot(0,x[8],'go')
plt.plot(0,x[9],'go')

plt.savefig("Images/slice60.jpg", dpi=200) 
plt.close()

x=df.iloc[:][90]
plt.plot(0,x[0],'go')
plt.plot(0,x[1],'bo')
plt.plot(0,x[2],'bo')
plt.plot(0,x[3],'go')
plt.plot(0,x[4],'bo')
plt.plot(0,x[5],'go')
plt.plot(0,x[7],'go')
plt.plot(0,x[8],'go')
plt.plot(0,x[9],'go')

plt.savefig("Images/slice90.jpg", dpi=200) 
plt.close()