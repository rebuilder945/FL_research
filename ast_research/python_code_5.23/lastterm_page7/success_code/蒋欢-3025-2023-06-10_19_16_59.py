ls=input().split()
dic={}
for x in ls:
    dic[x]=ls.count(x)
a=max(dic.values())
for key,value in dic.items():
    if value==a:
        print(key+" %d"%(value))
