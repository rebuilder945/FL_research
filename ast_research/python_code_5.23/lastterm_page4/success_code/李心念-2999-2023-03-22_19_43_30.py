a = input().split(" ")
b = input().split(" ")
c = eval(b[0])
d = eval(b[1])

if c<d:
    x = a[c]
    y = a[d]
    del a[c]
    del a[d-1]
    a.insert(c,y)
    a.insert(d,x)
    print(a)
else:
    m=d
    n=c
    x=a[m]
    y=a[n]
    del a[m]
    del a[n-1]
    a.insert(m,y)
    a.insert(n,x)
    print(a)
