import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

# 消除 output 的 warning
urllib3.disable_warnings()

# 宣告list(作為dataframe欄位)
title_list=[]
date_list=[]


payload={
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}
rs = requests.session()
pttpage = rs.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)

# 取2021/12/09 00:00至2022/01/09 15:00之文章標題 (共2920頁)
for page in range(38258,35356,-1):
  pttpage = rs.get("https://www.ptt.cc/bbs/Gossiping/index"+str(page)+'.html',verify=False)
  main = BeautifulSoup(pttpage.text,"html.parser")

  # 抓取每一頁文章標題及網址並用 OpenArticle() 抓取日期的數據
  for t,d in zip(main.select('.title'),main.select('.date')):
    date = d.text
    title = t.text
    if '刪除)' not in title:
        title = title.split(']')
        title_list.append(title[-1])
        date_list.append(date)
      
  
# list 轉 dataframe 並儲存成csv檔
df=pd.DataFrame({'title':title_list,'time':date_list})
df.to_csv('time.csv', index=False)
