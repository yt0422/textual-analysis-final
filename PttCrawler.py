import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

# 消除 output 的 warning
urllib3.disable_warnings()

# 宣告list(作為dataframe欄位)
title_list=[]
num_of_comment=[]
like=[]
dislike=[]

# 開啟每個文章並統計總留言數、推及噓總量的function
def OpenArticle(x):
  arrow=0
  like=0
  dislike=0
  reply=[]

  # 開啟文章網址
  payload={
      'from':'/bbs/Gossiping/index.html',
      'yes':'yes'
  }
  rs = requests.session()
  article = rs.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)
  article = rs.get(x,verify=False)
  main = BeautifulSoup(article.text, "html.parser")

  # 統計
  for t in main.select('.push'):
    a = t.text
    if a!='null':
      a = t.text.split(' ')
      if a[0]=='→':
        arrow+=1
      elif a[0]=='推':
        like+=1
      else:
        dislike+=1
  reply.append(arrow)
  reply.append(like)
  reply.append(dislike)
  return(reply)

payload={
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}
rs = requests.session()
pttpage = rs.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)

# 取2021/12/09 00:00至2022/01/09 15:00之文章標題 (共2920頁)
for page in range(38875,35954,-1):
  pttpage = rs.get("https://www.ptt.cc/bbs/Gossiping/index"+str(page)+'.html',verify=False)
  main = BeautifulSoup(pttpage.text,"html.parser")

  # 抓取每一頁文章標題及網址並用 OpenArticle() 抓取評論的數據
  for t in main.select('.title'):
    title = t.text
    if '刪除)' not in title:
      title = title.split(']')
      title_list.append(title[-1])
      href = "https://www.ptt.cc/" + t.a['href']
      comment=OpenArticle(href)[-3:]
      if sum(comment)>0:
        num_of_comment.append(sum(comment))
        like.append(comment[1])
        dislike.append(comment[2])
      else:
        num_of_comment.append(0)
        like.append(0)
        dislike.append(0)
  
# list 轉 dataframe 並儲存成csv檔
df=pd.DataFrame({'title':title_list,'comment':num_of_comment,'like':like,'dislike':dislike})
df.to_csv('display.csv', index=False)