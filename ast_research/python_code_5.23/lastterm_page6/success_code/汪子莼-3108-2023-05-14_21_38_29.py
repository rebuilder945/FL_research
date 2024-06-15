a=eval(input())
res={}
for i in a:
    for ch in i:
        if ch in res:
            res[ch]+=1
        else:
            res[ch]=1
newres=sorted(res.item(),key=lambda x:x[0])
for i in newres:
    print("%s,%d"%(i[0],i[1]))
