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
    x=a[d]
    y=a[c]
    del a[d]
    del a[c-1]
    a.insert(d,y)
    a.insert(c,x)
    print(a)
