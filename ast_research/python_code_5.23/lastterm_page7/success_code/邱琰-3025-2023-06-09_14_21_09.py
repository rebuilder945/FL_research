n=list(input().split())
dic={}
for i in n:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
m=0
for i in dic:
    if dic[i]>=m:
        m=dic[i]
dic2={}
for i in dic:
    if dic[i]==m:
        dic2[i]=m
dic2=sorted(dic2)
for i in dic2:
    print(i,m)
