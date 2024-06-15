a=input().split('')
dic={}
for i in dic:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
mn=max(dic.values())
mw=[k for k,v in dic.items() if v==mn]
mw.sort()
for i in mw:
    print(mw,mn)
