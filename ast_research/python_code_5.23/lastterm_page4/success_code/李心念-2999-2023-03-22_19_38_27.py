a = input().split(" ")
b = input().split(" ")
c = eval(b[0])
d = eval(b[1])
x = a[c]
y = a[d]
del a[c]
del a[d-1]
a.insert(c,y)
a.insert(d,x)
print(a)
