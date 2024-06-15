n = int(input())
x = 1
y = 2
v = []
for i in range(1,n+1):
    z = y/x
    y = x+y
    m = y-x
    x = m
    v.append(z)
    p = sum(v)
print("%.4f"%p)


