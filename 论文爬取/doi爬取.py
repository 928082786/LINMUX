# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:53:24 2019

@author: LINMUX
"""

import requests
from bs4 import BeautifulSoup
import re

def extra_archive(file):
   f=open(file)
   data=f.read()
   p= re.compile('.+?“(.+?)”')
   cate=p.findall(data)
   return cate

def extra_doi(keywords): 
    target='https://search.crossref.org/?q='+str(keywords)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    headers = {'User-Agent':user_agent}
    target=target.format(1)
    req=requests.get(url=target)
    html=req.text
    html=html.replace('<br>',' ').replace('<br/>',' ').replace('/>','>')
    bf=BeautifulSoup(html,"html.parser")
    texts=bf.find('div',class_='item-links-outer')
    texts_div=texts.find_all('div',class_='item-links')
    for item in texts_div:
        item_href=item.find('a')['href']
        return item_href
    
def archive_download(doi):
    return
    
    

file='desktop\\data.txt'   
cate=extra_archive(file)
cate=cate[9:]
doi={}
for item in cate: 
    try:
       doi[item]=extra_doi(item)
    except:
        doi[item]='None'
    
     
        