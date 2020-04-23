# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:35:06 2020

@author: neilw
"""

import sys
from PIL import Image

for i in range(10): 
    for j in range(1,17):
        stdvis="USEstdvis_trial_%d_keypoint_%d.jpg"%(i,j)
        matrices='titles.jpg'
        images = [Image.open(x) for x in [matrices,stdvis ]]
        
        widths, heights = zip(*(i.size for i in images))
        
        total_height = sum(heights)
        max_width = max(widths)
        
        new_im = Image.new('RGB', (max_width, total_height))
        
        y_offset = 0
        for im in images:
          new_im.paste(im, (0,y_offset))
          y_offset += im.size[1]
        
        new_im.save('titlestdvis_trial_%d_keypoint_%d.jpg'%(i,j))



   