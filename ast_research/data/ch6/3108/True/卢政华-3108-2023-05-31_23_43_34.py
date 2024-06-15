str=eval(input())
a={}
for i in str:
    for x in i:
        if x not in a:
            a[x]=1
        else:
            a[x]+=1
a=sorted(a.items())
v=list(a)
for x in a:
    print("%s,%d"%(x[0],x[1]))
