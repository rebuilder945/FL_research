lst=eval(input())
d={}
for x in lst:
    for i in x:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
d=sorted(d.items(),key=lambda x:x[0])
s=[list(x) for x in s]
for x in s:
    print("%s,%d"%(x[0],x[1]))
    
