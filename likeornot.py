import pandas as pd
df=pd.read_csv('./data/result.csv')
like=df['like']
dislike=df['dislike']
x=len(like)
title=[]
per=[]
for i in range(x):
    if df.iloc[i][1]!=0 and df.iloc[i][2]!=0:
        if df.iloc[i][3]/df.iloc[i][2]>=2 and df.iloc[i][1]>50:
            title.append(df.iloc[i][0])
            per.append(100*round(df.iloc[i][3]/(df.iloc[i][3]+df.iloc[i][2]),2))
df=pd.DataFrame({'title':title,'percentage of dislike':per})
df.to_csv('dontlike.csv', index=False)