n=map(list,input().split())
dic={}
for i in n:
    if i not in list(dic.keys()):
        dic[i]=1
    else:
        dic[i]+=1
m=0
for i in list(dic.keys()):
    if dic[i]>=m:
        m=dic[i]
dic2={}
for i in list(dic.keys()):
    if dic[i]==m:
        dic2[i]=m
dic2=sorted(dic2)
for i in list(dic2.keys()):
    print(i,dic2[i])
