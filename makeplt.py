import matplotlib.pyplot as plt
import sys
import pandas as pd
sys.path.append("event_count.py")
from event_count import count

x=count.keys()
a=count.values()
w=[]
p=[]
r=[]
c=[]
s=[]
m=[]
for i in a:
    w.append(i[0])
    p.append(i[1])
    r.append(i[2])
    c.append(i[3])
    s.append(i[4])
    m.append(i[5])
    
y1=w
y2=p
y3=r
y4=c
y5=s
y6=m
plt.figure(figsize=(70,40))
plt.plot(x, y1, marker = "o", label = 'homhom')
plt.plot(x, y2, marker = "o", label = 'political')
plt.plot(x, y3, marker = "o", label = 'referendum')
plt.plot(x, y4, marker = "o", label = 'COVID-19')
plt.plot(x, y5, marker = "o", label = 'social event')
plt.plot(x, y6, marker = "o", label = 'movie')
plt.legend(loc = 'upper right')
plt.ylabel("Frequency")
plt.xlabel("Date")
plt.xticks(rotation=45,fontsize=7)
plt.show()

print(a)