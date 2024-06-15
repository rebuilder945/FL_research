strlst=eval(input())
res={}
for stri in strlst:
    for ch in stri:
        if ch in res:
            res[ch]+=1
        else:
            res[ch]=1
newres=sorted(res.items(),key=lambda x:x[0])
for stri in newres:
    print("%s,%d"%(stri[0]stri[1]))
