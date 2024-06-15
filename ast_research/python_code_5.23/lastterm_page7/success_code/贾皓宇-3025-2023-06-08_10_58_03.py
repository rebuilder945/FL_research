a=list(input().split())
lstnum=[]
dic={}
for x in a:
    lstnum.append(a.count(x))
    dic[x]=a.count(x)
m=max([dic[i] for i in dic])
lst=[]
for x in dic:
    lst.append(x)
lst.sort()
for x in lst:
    if dic[x]==m:
        print(x,dic[x]) 
