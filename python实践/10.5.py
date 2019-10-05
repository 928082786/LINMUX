# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:40:41 2019

@author: LINMUX
"""
"""
主要包括： 1.堆的pop和push，根据优先级的大小pop
          2.Removing Duplicates from a Sequence while Maintaining Order 
          3."Determining the Most Frequently Occurring Items in a Sequence"
          4." Grouping Records Together Based on a Field " 
"""
#############################################################################
"""q = PriorQueue()
                q.push(1,Item('foo')) 
                q.push(5,Item('bar')) 
                q.push(2,Item('spam')) 
                q.push(3,Item('grok'))
        q.queue=
                [(1, 0, item('foo')),
                 (3, 3, item('grok')),
                 (2, 2, item('spam')),
                 (5, 1, item('bar'))]
                """
import heapq

class PriorQueue:
    def __init__(self):
        self.queue=[];
        self.index=0
    def push(self,Priority,item):
        heapq.heappush(self.queue,(Priority,self.index,item))
        self.index+=1
    def pop(self):
       return heapq.heappop(self.queue)[-1]
        
class Item:
    def __init__(self,name):
        self.name=name
    def __repr__(self):          
       return 'item({!r})'.format(self.name) #str.format()用于填充字符串
   

###############################################################################



"Removing Duplicates from a Sequence while Maintaining Order " 
###############################################################################
#注意到yield函数的特殊用法
 
"""对于set()也有同样的作用，但是set后的list是无序的
例如：
a = [1, 5, 2, 1, 9, 1, 5, 10]
set(a)=[1, 2, 5, 9, 10]
"""     
def dedupe(items):
    seen=set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            
###############################################################################



"Determining the Most Frequently Occurring Items in a Sequence"  
###############################################################################
from collections import Counter 
       
words = [   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 
         'my', 'eyes', "you're", 'under' ]
words_count=Counter(words)
max(zip(words_count.values(),words_count.keys()))          
###############################################################################




" Grouping Records Together Based on a Field " 
###############################################################################
from operator import itemgetter
from itertools import groupby

rows = [{'address': '5412 N CLARK', 'date': '07/01/2012'}, 
        {'address': '5148 N CLARK', 'date': '07/04/2012'}, 
        {'address': '5800 E 58TH', 'date': '07/02/2012'},  
        {'address': '2122 N CLARK', 'date': '07/03/2012'},  
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, 
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},   
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},  
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
        ]

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):    
    print(date)    
    for i in items:        
        print('    ', i)  
        
###############################################################################
















           