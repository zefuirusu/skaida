#!/usr/bin/env python
# encoding='utf-8'
# 读取网址的txt文件,转化成JavaScript脚本,复制到浏览器直接打开.
# 只要该脚本所在目录下有一名为"inlinks.txt"的文件，每行写一个url，就会生成一个名为"openlinks-jss.txt"的javascript脚本，放到浏览器中运行即可批量打开链接。

#indir=input('=>type in the directory of the text file containing links: ')
# indir=r'D:\HZ.SK\MissionAccomplished\Project 数据\links.txt'
#outdir=input('=>type in the outputing directory of the javascript file: ')

indir=r'./inlinks.txt'
outdir=r'./'

import re
import os

linkli=[]
with open(indir) as f:
    a=f.readlines()
    for i in a:
        b=re.sub(r'\n$',r'',i)
        linkli.append(b)
#
# print(linkli)
#for i in linkli:
#    print(i)
outna=r'openlinks-js'+r'.txt'
outnadir=os.path.join(os.path.abspath(outdir),outna)
with open(outnadir,'a') as g:
    g.write(r'var li=[')
    j=0
    while j< len(linkli):
        g.write(r'"')
        g.write(linkli[j])
        if j!=len(linkli)-1:
            g.write(r'",')
        else:
            g.write(r'"')
        j+=1
    g.write('];\n')
    g.write('var lilen=li.length;')
    g.write('\n')
    g.write('for (var i=lilen-1;i>-1;i--){')
    g.write('\n')
    g.write('\t')
    g.write('var li_fake=li[i];')
    g.write('\n')
    g.write('\t')
    g.write('window.open(li_fake);')
    g.write('\n')
    g.write('\t')
    g.write('};')
    g.write('\n')
