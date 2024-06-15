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
    dd.sort()
    return(dd)
a=input()
a=list(a.split(" "))
n,m=eval(a[0]),eval(a[1])
if type(n)!=int or type(m)!=int or n<0 or m<0 or m-n<3 or n<=10 or m>=10:
    print("illegal input")
else:
    for i in ddd(n,m):
        print(i,end=" ")
