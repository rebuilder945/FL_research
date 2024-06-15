a=list(input().split())
lstnum=[]
dic={}
for x in a:
    lstnum.append(a.count(x))
    dic[x]=a.count(x)
m=max([dic[i] for i in dic])
for x in dic:
    if dic[x]==m:
        print(x,dic[x])
