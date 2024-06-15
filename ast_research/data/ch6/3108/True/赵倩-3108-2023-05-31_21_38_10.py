a=eval(input())
c={}
for str in a:
    for y in str:
        if y not in c:
            c[y]=1
        else:
            c[y]=c[y]+1
for i in sorted(c.keys()):
    print("%s,%d"%(i,c[i]))



