cnt=0
res=["None"]
dic={}
lst=list(input().split())
for i in range(len(lst)):
    dic[lst[i]]=dic.get(lst[i],0)+1
for k,v in dic.items():
    if v>cnt:
        cnt=v
        res=[k]
    elif v==cnt:
        res.append(k)
res.sort()
for i in range(len(res)):
    print(res[i],cnt)
