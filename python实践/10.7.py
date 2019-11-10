# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:38:35 2019

@author: LINMUX
"""
"""
1. Extracting a Subset of a Dictionary 
"""

'1. Extracting a Subset of a Dictionary '
################################################################################
prices = {   'ACME': 45.23,  
             'AAPL': 612.78,
             'IBM': 205.55,
             'HPQ': 37.20,
             'FB': 10.75 }
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }

p1={key:value for key,value in prices.items()if value>200}
p2={key:value for key,value in prices.items()if key in tech_names}
################################################################################

################################################################################
import collections