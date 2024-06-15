lst=eval(input())
c={}
for str in lst:
    for x in str:
        c[x]=c.get(d,0)+1
for i in sorted(c.keys()):
    print("%s","%d"%(i,c[i]))
