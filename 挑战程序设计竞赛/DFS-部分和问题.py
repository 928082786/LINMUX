# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

#DFS 部分和问题
import numpy as np
def dfs(i,sum):
    if i==n:
        return sum==k        
    if dfs(i+1,sum):
        return True
    if dfs(i+1,sum+a[i]):
        return True
    return False

def slove():
    if dfs(0,0):
      print('yes')
    else:
      print('no')
      
  
#n=4
#k=15
#a=[1,2,4,6]
a=input('你要输入的数组是：')
k=input('你要输入的整数是：')
a=a.split()
n=np.size (a)
for i in range(0,n-1):
  a[i]=np.int(a[i])
a=np.array(a) 
slove()