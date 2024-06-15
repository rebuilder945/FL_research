lst=eval(input())
s={}
for x in sums:
    for i in x:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
s=sorted(s.items(),key=lambda x:x[0])
s=[list(x) for x in s]
for x in s:
    print("%s,%d"%(x[0],x[1]))
