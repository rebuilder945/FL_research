sums=eval(input())
s={}
for x in sums:
    for i in x:
        s[i] = s.get(i,0) + 1
s=sorted(s.items(),key=lambda x:x[0])
s=[list(x) for x in s]
for x in s:
    print("%s,%d"%(x[0],x[1]))
