#!/usr/bin/env python
# coding: utf-8

import datetime
import pandas as pd
import requests as res

class searchInfo:
    def __init__(self,quickdir):
        self.quickdir=quickdir
        bm=pd.read_excel(quickdir,sheet_name='en')
        bmcomli=bm.loc[:,'CompanySearchName'].dropna() # company name list to search.
        kwsk=bm.loc[:,'kwsk'].dropna() # key word
        self.bmcomli=list(bmcomli) # basic main company name list.
        self.kwsk=list(kwsk)
        return
    def readkw(self): # read and tranform keyword to search.
        qkw=[] # quick key word
        for i in self.bmcomli:
            for j in self.kwsk:
                b=str(i)+r' '+str(j)
                qkw.append(b)
                continue
            continue
        self.search_keyword=qkw # search keyword is the quick keyword.
        return qkw
    def getSiteli(self):
        t1=datetime.datetime.now()
        siteli=[]
        for i in self.readkw():
            # 谷歌搜索
            #r1=res.get(r'https://www.google.com/search?source',params={'q':i,'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
            # duckduckgo 搜索
            # r1=res.post(r'https://duckduckgo.com/',params={'q':i,'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
            # startpage 搜索
            #r1=res.get(r'https://www.startpage.com/do/search',params={'query':i,'User-Agent':r'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
            # 瑞典牛搜索
            r1=res.post(r'https://swisscows.ch/?culture=en',params={'query':i,'User-Agent':r'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
            # 谷歌新闻：
            # r1=res.get(r'https://www.google.com/search?source',params={'q':i,'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0','tbm':'nws'})
            # snopyta 搜索
            # r1=res.post(r'https://search.snopyta.org/',params={'q':i,'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'})
            #
            r2=r1.url
            siteli.append(r2)
            continue
        t2=datetime.datetime.now()
        self.request_time=t2-t1
        self.url_to_open=siteli
        return siteli
    #
#
from selenium import webdriver
option = webdriver.ChromeOptions()
#r'C:\Users\aaa\AppData\Local\Google\Chrome\User Data\Defaul'
#option.add_argument(r'--incognito')
#option.add_argument(r'--disable-javascript')
#option.add_argument(r'--user-data-dir=C:\Users\aaa\AppData\Local\Google\Chrome\User Data\Defaul')
#option.add_extension(r'D:\HZ.SK\tools\Chrome插件\ClusterTabManager\2.2.3_0.crx')
#option.add_extension(r'D:\HZ.SK\tools\Chrome插件\ClusterTabManager\2.2.3_0.crx')
#option.add_extension(r'D:\HZ.SK\tools\Chrome插件\OneTab\1.18_0.crx')
class Chr(webdriver.Chrome):
    def goto(self,one_site):
        js=r"window.open("+r'"'+one_site+r'")'
        #print(js)
        self.execute_script(js)
        return
    def gotomany(self,siteli):
        t3=datetime.datetime.now()
        for i in siteli:
            self.goto(i)
        handles=self.window_handles
        self.switch_to.window(handles[0])
        self.close()
        self.switch_to.window(handles[0])
        t4=datetime.datetime.now()
        self.open_pages_spent=t4-t3
        print(r'pages opened:',len(siteli))
        return
#
if __name__=='__main__':
    quickdir=r'./AutoSearch.xlsx'
    sinfo1=searchInfo(quickdir)
    print(sinfo1.getSiteli())
    s1=Chr(options=option)
    s1.gotomany(sinfo1.getSiteli())
    print('request time spent:',sinfo1.request_time)
    print('pages open time spent:',s1.open_pages_spent)
    pass

