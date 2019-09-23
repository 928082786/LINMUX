# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:47:43 2019

@author: XT
"""
import cv2
import numpy as np
import time
from scipy.spatial.distance import pdist, squareform



def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = 2)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0,0,0), thickness = 1)
        cv2.imshow("image", img)
        num[count[0]]=x,y
        count[0]=count[0]+1
       
def distance_compute(num,choose):
      ab = pdist([num[0],num[1]], 'euclidean')  
      bc = pdist([num[1],num[2]], 'euclidean')
      cd = pdist([num[2],num[3]], 'euclidean')
    #  dv = pdist([num[3],num[4]], 'euclidean')
      if choose==1:
           dv = pdist([num[3],num[4]], 'euclidean')
           result=(ab+bc)*(bc+cd+dv)/((ab+bc+cd+dv)*bc)
      if choose==2:
           dv = pdist([num[3],num[4]], 'euclidean')
           result=(bc+cd+dv)*cd/((bc+cd)*(cd+dv)-(bc+cd+dv)*cd)
      return result
   
def remark(img):
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
        cv2.imshow("image", img)
        cv2.waitKey(0)

def draw_miexian(p,img):
    p_num=np.size(p)
    for i in range(1,np.int(p_num/2)):
        cv2.line(img,(0,np.int(p[i][1])),(1500,np.int(1500*p[i][0]+p[i][1])),(255, 0, 0), thickness = 2)

def find_miedian(p):
    p_num=np.size(p)
    return p[np.int(p_num/2)-1]

def step1():
    remark(img)
    np.savetxt('C:\\Users\\XT\\Desktop\\2.csv', num, delimiter = ',') 
    time.sleep(5)
    temp=np.loadtxt('C:\\Users\\XT\\Desktop\\p.csv', delimiter = ',') 
#    draw_miexian(temp,img)
    p=find_miedian(temp)
    return p

def step2(n,p):
#    remark(img)
    num[np.int(count):np.int(count)-1+n]=p[0:n-1]
    result1=distance_compute(num,1)
    result2=distance_compute(num,2)
    result=result1*4.7+4.7/(result2-1)
    return result

n=2
p=np.zeros((n,2))
for i in range(0,n):
  img = cv2.imread("C:\\Users\\XT\\Desktop\\2-1.png")
  img = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
  count=np.zeros(1,int)
  num=np.zeros((100,2)) 
  p[i]=step1()
  
result=step2(n,p) 
