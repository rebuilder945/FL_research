lst=eval(input())
s={}
for x in lst:
    for i in x:
        if i not in s:
            s[i]=1
        else:
            s[i]+=1
s=sorted(s.items(),key=lambda x:x[0])
lst2=[list(x) for x in s]
for x in lst2:
    print("%s,%d"%(x[0],x[1]))

