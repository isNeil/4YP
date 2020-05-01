# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:18:32 2020

@author: neilw
"""
from PIL import Image
import cv2

#background = Image.open("3-1.png_segment.jpg")
#overlay = Image.open("3-2.png_segment.jpg")
#
#background = background.convert("RGBA")
#overlay = overlay.convert("RGBA")
#
#new_img = Image.blend(background, overlay, 0.5)
#new_img.save("blend3segment.png","PNG")

import matplotlib.pyplot as plt

name='3-1.png'
nemo = cv2.imread(name)
nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
#plt.imshow(nemo)
#plt.show()
hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
lower_range = (20, 20, 60)
upper_range = (35, 255, 255)
#lower_range = (26, 25, 60)
#upper_range = (100, 255, 255)

mask = cv2.inRange(hsv_nemo, lower_range, upper_range)

result = cv2.bitwise_and(nemo, nemo, mask=mask)
plt.figure(figsize=(19.2,10.8))
#plt.subplot(1, 2, 1)
#plt.imshow(mask, cmap="gray")
#plt.subplot(1, 2, 2)
plt.imshow(result)
plt.axis('off')
plt.tight_layout()

ax = plt.gca()

ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())
plt.savefig(name+'_segment.jpg', dpi=100, pad_inches = 0)  
