sums=eval(input())
n={}
for x in sums:
    for i in x:
        if i not in n:
            n[i]=1
        else:
            n[i]+=1
n=sorted(n.items(),key=lambda x:x[0])
n=[list(x) for x in n]
for x in n:
    print("%s,%d"%(x[0],x[1]))
