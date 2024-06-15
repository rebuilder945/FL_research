a = input().split(" ")
c = input().split(" ")
b = a.copy()
a[int(c[0])]=b[int(c[1])]
a[int(c[1])]=b[int(c[0])]
print(a)
