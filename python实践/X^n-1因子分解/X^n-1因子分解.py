# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:18:32 2019

@author: LINMUX
"""

import numpy as np

from sympy.polys.domains import ZZ 
from sympy.polys.galoistools import gf_factor as factor


def print_x1(arr):
    temp=''
    length=len(arr)
    for i in range(0,length):
        if arr[i] !=0:
            temp=temp+str(arr[i])+'x^'+str(length-i-1)+'+'
#    print(temp[:-1]) 
    temp='('+temp[:-1]+')'
    f.write(temp)

def print_x2(arr):
    temp=''
    temp='('+'多项式'+str(arr[0])+','
    temp=temp+('指数'+str(arr[1])+')')
#    print(temp[:-1]) 
#    temp='('+temp[:-1]+')'
    f.write(temp)

#def factor_poly(a):
#    a=a+1
#    poly={}
#    factor_p={}
#    for iter in range(2,a+1):
#        poly[iter-1]=np.zeros(iter,dtype=np.int32)
#        poly[iter-1][0]=1
#        poly[iter-1][-1]=1
#        factor_p[iter-1]=factor(ZZ.map(poly[iter-1]),2,ZZ)
#    return factor_p    
#
#
#def print_poly(factor_p):
#    num=factor_p.__len__()
#    for iter in range(1,num+1):
#        print(str(iter))
#        factor_temp=factor_p[iter][1]
#        length=len(factor_temp)
#        for i in range(0,length):
#            print('&')
#            print_x(factor_temp[i][0])
#            
 
_print_methods = {
    'print_x1': print_x1, 
    'print_x2': print_x2,  
}
           
def simple_factor(a,method='print_x2'):
    poly=np.zeros(a+1,dtype=np.int32)
    poly[0]=1
    poly[-1]=1
    factor_p=factor(ZZ.map(poly),5,ZZ)
    factor_temp=factor_p[1]
    length=len(factor_temp)
    for i in range(0,length):
        _print_methods[method](factor_temp[i])
        
def main(x):
    for i in range(1,x+1):
        temp='x^'+str(i)+'-1:'
        f.write('\n'+temp)
        print(i)
        simple_factor(i)

f=open('D:\LINMUX\code\data\data2-3.txt','w')
main(100)
#simple_factor(19)
f.close()
