ls=input().split()
dic={}
ls2=[]
for x in ls:
    dic[x]=ls.count(x)
a=max(dic.values())
for key,value in dic.items():
    if value==a:
        ls2.append(key+" %d"%(value))
ls2.sort()
for i in ls2:
    print(i)
