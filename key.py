import pandas as pd

w=[]
p=[]
r=[]
c=[]
s=[]
m=[]

kw = pd.read_csv('keyword.csv', encoding='utf-8')
kw = kw.fillna('0')
wang=kw['王力宏']
pltc=kw['政治']
re=kw['公投']
cor=kw['疫情']
soc=kw['社會']
mov=kw['影視']
for i in wang:
    if i!='0':
        w.append(i)
for i in pltc:
    if i!='0':
        p.append(i)
for i in re:
    if i!='0':
        r.append(i)
for i in soc:
    if i!='0':
        s.append(i)
for i in mov:
    if i!='0':
        m.append(i)

