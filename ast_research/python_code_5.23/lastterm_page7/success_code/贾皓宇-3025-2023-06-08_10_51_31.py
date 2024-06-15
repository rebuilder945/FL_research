a=list(input().split())
lstnum=[]
dic={}
for x in a:
    lstnum.append(a.count(x))
    dic[x]=a.count(x)
m=max([dic[i] for i in dic])
k=list(dic.keys()).sort()
for x in k:
    if dic[x]==m:
        print(x,dic[x])
