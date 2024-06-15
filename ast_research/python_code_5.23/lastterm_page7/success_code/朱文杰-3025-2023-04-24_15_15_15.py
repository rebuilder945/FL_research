Str=input().split()
dic={}
for i in Str:
    dic[i]=dic.get(i,0)+1
ls=list(dic.values())
ls2=list(dic.items())
ls2.sort(key=lambda x:x[0])
for k,v in ls2:
    if v==max(ls):
        print(k,v)
