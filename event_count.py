import sys
import pandas as pd
sys.path.append("key.py")
from key import w,s,r,p,m,c

df = pd.read_csv('date.csv', encoding='utf-8')
title=df['title']
date=df['date']
end=len(date)

countkey=list(set(date))
countkey_sort=sorted(countkey)
countkey=countkey_sort[9:]
for i in countkey_sort[0:9]:
    countkey.append(i)

count={}
for i in countkey:
    count[i]=[0,0,0,0,0,0]

for i in range(end):
    y=count[date[i]]
    for j in w:
        if j in title[i]:
            y[0]+=1
    for j in p:
        if j in title[i]:
            y[1]+=1
    for j in r:
        if j in title[i]:
            y[2]+=1
    for j in c:
        if j in title[i]:
            y[3]+=1
    for j in s:
        if j in title[i]:
            y[4]+=1
    for j in m:
        if j in title[i]:
            y[5]+=1

print(count)
"""for i in range(end):
    if ' ' in title[i]:
        newtitle=''
        title[i]=title[i].split(' ')
        for j in title[i]:
            newtitle+=j
        if i==end-1 or date[i+1] != date[i] :
            s+=newtitle+'\n'
        
        else:
            s+=newtitle
"""
