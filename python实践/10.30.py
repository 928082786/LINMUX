# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:29:42 2019

@author: LINMUX
"""

import numpy as np

class sequence():
    def __init__(self,name,seq):
        self.name=name
        self.seq=seq
           
    def renew_name(self,x):
        self.name.append(x)
        return self.name
        
        
def vec_dic(vector):
    n=np.size(vector)
    dic={}
    for i in range(0,n):
        dic[vector[i]]=vector[(i+1)%n]
    return dic

def same_vec(x,y):
    len_x=len(x)
    len_y=len(y)
    if len_x>len_y:
        for i in x.keys():
           if i not in y.keys():
              y[i]=i
    else:
        for i in y.keys():
           if i not in x.keys():
               x[i]=i
    return [x,y]       


def rotate_f(x,y):
    r_dic={}
    same_vec(x,y)
    for i in y.keys():
        if y[i] in x.keys():
            r_dic[i]=x[y[i]]
        else:
            r_dic[i]=y[i]
    return r_dic



def disturb(order,x):
    order_x=rotate_f(order.seq,x)
    if order_x in sequence_class.values.seq:
        return;
    temp=sequence(order.name,order_x)
    sequence_class[sequence_class.__len__()+1]=temp
    sequence_class[sequence_class.__len__()+1].renew_name(x)
    
def disturb_xy(order,x,y):
    
    disturb(order,x)
    disturb(order,y) 
    
def generate_set(x,rotate1,rotate2):
    disturb_xy(x,rotate1,rotate2)
    generate_set(sequence_class[-2],rotate1,rotate2)
    generate_set( sequence_class[-1],rotate1,rotate2)
    
   
    
rotate1=[1,3,4,2]
rotate2=[1,2]
dic1=vec_dic(rotate1)
dic2=vec_dic(rotate2)
#[dic1,dic2]=same_vec(dic1,dic2)
sequence_class={}
a=sequence([''],[1,2,3,4])
sequence_class[0]=a
generate_set(a,rotate1,rotate2)