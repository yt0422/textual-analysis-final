import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

# 消除 output 的 warning
urllib3.disable_warnings()

# 宣告List容器
title_list=[]
post=[]
comment=[]

# 開啟每個文章並抓取留言及內文的function
def OpenArticle(x):

    # 開啟文章網址
    payload={
        'from':'/bbs/Gossiping/index.html',
        'yes':'yes'
    }
    rs = requests.session()
    article = rs.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)
    article = rs.get(x,verify=False)
    main = BeautifulSoup(article.text, "html.parser")

    # 利用split取內文
    time=main.select('.article-meta-value')[-1].text
    year=time[-4:]
    post=main.text.split('--')[0]
    post=post.split(str(year))[-1]
    comment=""

    # 把評論串成字串
    for t in main.select('.push-content'):
        if t!='null':
            a = t.text.split(':')[-1]
            comment=comment+a+'\n'
    data=[]
    data.append(post)
    data.append(comment)
    return data

payload={
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}
rs = requests.session()
pttpage = rs.post('https://www.ptt.cc/ask/over18',verify=False,data=payload)

# 取2021/12/09至2022/01/09之文章標題
for page in range(38215,35356,-1):
  pttpage = rs.get("https://www.ptt.cc/bbs/Gossiping/index"+str(page)+".html",verify=False)
  main = BeautifulSoup(pttpage.text,"html.parser")

  # 抓取每一頁王力宏相關文章(關鍵詞來自共現分析與N字詞)標題及網址並用 OpenArticle() 抓取資料
  for t in main.select('.title'):
    title = t.text
    if '刪除)' not in title and ('王力宏' in title or '李靚蕾' in title or '靚蕾' in title or '力宏' in title or '宏宏' in title or '蕾神' in title or '徐若瑄' in title):
      title = title.split(']')
      title_list.append(title[-1])
      href = "https://www.ptt.cc/" + t.a['href']
      data=OpenArticle(href)
      post.append(data[0])
      comment.append(data[1])
      
  
# list 轉 dataframe 並儲存成csv檔
df=pd.DataFrame({'title':title_list,'article':post,'comment':comment})
df.to_csv('test.csv', index=False)