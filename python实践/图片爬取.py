# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 18:04:50 2019

@author: LINMUX
"""

import requests
from bs4 import BeautifulSoup
import re
import urllib.request
 
def find_img(target):
    req=requests.get(url=target)
    html=req.text
    html=html.replace('<br>',' ').replace('<br/>',' ').replace('/>','>')
    bf=BeautifulSoup(html,"html.parser")

    texts=bf.find('div',id='article')
    texts_div=texts.find_all('iframe',id='pdf')
    texts_div=str(texts)
    p= re.compile(r'src=(.+?)#')
    pdf_url=str(p.findall(texts_div))
    pdf_url=pdf_url[3:-2]
    return pdf_url+'?download="true"'
    
def extra_img_url(img_target): 
    req=requests.get(url=img_target)
    html=req.text
    html=html.replace('<br>',' ').replace('<br/>',' ').replace('/>','>')
    bf=BeautifulSoup(html,"html.parser")
    texts=bf.find('img',id)
    p= re.compile(r'src=(.+?)/>')
    img_url=str(p.findall(str(texts)))
    return 'https://zero.sci-hub.tw'+img_url[3:-3]

def extra_img(img_target):
    img_name='1.jpg'
    path='desktop//'+img_name
    r = requests.get(img_target)
    r.raise_for_status()
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print("文件保存成功")
            

def extra_pdf(pdf_url):
    file_name = pdf_url.split('/')[-1]
    u=urllib.request.urlopen(pdf_url)
    f = open('desktop\\'+file_name, 'wb')

    block_sz = 8192
    while True:
         buffer = u.read(block_sz)
         if not buffer:
              break
    f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)


#target="https://zero.sci-hub.tw/204/c5a1c6e9100f47ca30367ce3f286091c/hellesth1992.pdf?download=true"
#https://zero.sci-hub.tw/img/5dfcdac37f97a.jpg
target='https://sci-hub.tw/https://doi.org/10.1016/0012-365x(92)90553-r#'
img_target=find_img(target)
img_url=extra_img_url(img_target)
u='https://cn.bing.com/images/search?view=detailV2&ccid=Ha2sSXDA&id=1E348DAA67711E1AEB8B85F4B79BB0E0ADE2F6A7&thid=OIP.Ha2sSXDAYxEfGQolyp97zAHaEg&mediaurl=http%3a%2f%2fpic.lvmama.com%2fuploads%2fpc%2fplace2%2f2017-03-29%2f16398d83-b15b-4038-bbba-bbe9caab36bf.jpg&exph=1247&expw=2048&q=%e6%be%b3%e9%97%a8%e7%be%8e%e6%99%af&simid=608054170276597527&selectedIndex=0&ajaxhist=0'
extra_img(u)