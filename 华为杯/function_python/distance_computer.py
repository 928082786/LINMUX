# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
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
       
def distance_compute(num):
  m = pdist([num[0],num[1]], 'euclidean')
  n = pdist([num[1],num[2]], 'euclidean')
  u = pdist([num[2],num[3]], 'euclidean')
  v=  pdist([num[3],num[4]], 'euclidean')
  result=(m+n+u)*(n+u+v)*(u+v)/(v*(m+n+u+v)*n)*4.8
  return result

def position_compute(num):
     m = pdist([num[0],num[1]], 'euclidean')
     n = pdist([num[1],num[2]], 'euclidean')
     u = pdist([num[2],num[3]], 'euclidean')
     cr=(m+n)*(n+u)/((m+n+u)*n)
     result=1.55*cr
#     result=1.55*cr/(cr-1)
     return result
     
img = cv2.imread("C:\\Users\\XT\\Desktop\\1.png")       
count=np.zeros(1,int)
num=np.zeros((5,2))    
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)

#while(True):
#    try:
#        if cv2.waitKey()==27:
#            exit
#    except Exception:
#        cv2.waitKey()
#        break
        
cv2.waitKey(0)
distance_result=distance_compute(num)
position_result=position_compute(num)
cv2.destroyAllWindow()


