#!/usr/bin/env python
# coding: utf-8

#import os
#import re
import datetime
#import numpy as np
import pandas as pd
import requests as res


quickdir=r'./AutoSearch.xlsx'
bm=pd.read_excel(quickdir,sheet_name='en')

bmcomli=bm.loc[:,'CompanySearchName'].dropna()
kwsk=bm.loc[:,'kwsk'].dropna()

bmcomli=list(bmcomli)
kwsk=list(kwsk)
print(kwsk)

from selenium import webdriver

option = webdriver.ChromeOptions()
#r'C:\Users\aaa\AppData\Local\Google\Chrome\User Data\Defaul'
#option.add_argument(r'--incognito')
#option.add_argument(r'--disable-javascript')
#option.add_argument(r'--user-data-dir=C:\Users\aaa\AppData\Local\Google\Chrome\User Data\Defaul')
#option.add_extension(r'D:\HZ.SK\tools\Chrome插件\ClusterTabManager\2.2.3_0.crx')
#option.add_extension(r'D:\HZ.SK\tools\Chrome插件\ClusterTabManager\2.2.3_0.crx')
#option.add_extension(r'D:\HZ.SK\tools\Chrome插件\OneTab\1.18_0.crx')

# 发送链接
qkw=[]
for i in bmcomli:
    for j in kwsk:
        b=str(i)+r' '+str(j)
        qkw.append(b)
#
t1=datetime.datetime.now()
siteli=[]
for i in qkw:
    # 谷歌搜索
    #r1=res.get(r'https://www.google.com/search?source',params={'q':i,'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
    # duckduckgo 搜索
    # r1=res.post(r'https://duckduckgo.com/',params={'q':i,'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
    # startpage 搜索
    #r1=res.get(r'https://www.startpage.com/do/search',params={'query':i,'User-Agent':r'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
    # 瑞典牛搜索
    #r1=res.post(r'https://swisscows.ch/?culture=en',params={'query':i,'User-Agent':r'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
    # 谷歌新闻：
    # r1=res.get(r'https://www.google.com/search?source',params={'q':i,'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0','tbm':'nws'})
    # snopyta 搜索
    r1=res.post(r'https://search.snopyta.org/',params={'q':i,'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
    #
    r2=r1.url
    siteli.append(r2)
#
t2=datetime.datetime.now()

# s1=ska.Scha(options=option)
# s1.opsite(siteli)

class Chr(webdriver.Chrome):
    def goto(self,one_site):
        js=r"window.open("+r'"'+one_site+r'")'
        #print(js)
        self.execute_script(js)
    def gotomany(self,siteli):
        for i in siteli:
            self.goto(i)
        handles=self.window_handles
        self.switch_to.window(handles[0])
        self.close()
        self.switch_to.window(handles[0])
#
s1=Chr(options=option)
s1.gotomany(siteli)

t3=datetime.datetime.now()
#print(t1)
#print(t2)
print(r'request time spent',t2-t1)
print(r'open pages time spent',t3-t2)
print(r'total time spent:',t3-t1)
print(r'pages opened:',len(siteli))

del qkw
del t1
del siteli
del t3
del quickdir
del bm
del bmcomli
del kwsk
