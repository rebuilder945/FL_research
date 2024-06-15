def ddd(n,m):
    x=[]
    y=[]
    z=[]
    d=[]
    dd=[]
    for i in range(n,m):
        x.append(i)
        y.append(i)
        z.append(i)
    for a in x:
        y.remove(a)
        z.remove(a)
        for b in y:
            z.remove(b)
            for c in z:
                d.append(str(a)+str(b)+str(c))
            z.append(b)
        y.append(a)
        z.append(a)
    for i in d:
        i=int(i)
        if i>=100:
            dd.append(i)
    return(dd)
a=input()
a=list(a.split(" "))
n,m=eval(a[0]),eval(a[1])
for i in ddd(n,m):
    print(i,end=" ")
