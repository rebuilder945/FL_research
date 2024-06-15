lst = eval(input())
s={}
for i in lst:
    for x in i:
        if x not in s:
            s[x]=1
        else:
            s[x]+=1
s=sorted(s.items(),key=lambda x:x[0])
s=[list(s)]
for x in s:
    print("%s,%d"%(x[0],x[1]))
