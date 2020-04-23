# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:35:06 2020

@author: neilw
"""

import sys
from PIL import Image

images = [Image.open(x) for x in ['MEASUREmatrix.jpg', 'MEASUREmatrixVAR.jpg', 'Test3.jpg']]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test.jpg')