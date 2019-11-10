# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:12:04 2019

@author: LINMUX
"""

'''
 1.Combining Multiple Mappings into a Single Mapping 
'''

'1.Combining Multiple Mappings into a Single Mapping '
##############################################################################
from collections import ChainMap 

a = {'x': 1, 'z': 3 } 
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b) 
print(c['x'])      # Outputs 1  (from a) 
print(c['y'])      # Outputs 2  (from b) 
print(c['z'])      # Outputs 3  (from a)

'''
    merged = dict(b) 
    merged.update(a)
   >>> a['x'] = 13 
   >>> merged['x'] =1
   
   A ChainMap uses the original dictionaries
   >>> merged = ChainMap(a, b) 
   >>> merged['x'] 1 
   >>> a['x'] = 42 
   >>> merged['x']   # Notice change to merged dicts 
   >>> merged['x']=42 
   '''


