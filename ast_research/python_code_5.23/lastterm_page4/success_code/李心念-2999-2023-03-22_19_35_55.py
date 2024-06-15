a = input().split(" ")
b = input().split(" ")
c = eval(b[0])
d = eval(b[1])
x = a[c]
y = a[d]
del a[c]
del a[d-1]
a.insert(c,x)
a.insert(d,y)
print(a)
