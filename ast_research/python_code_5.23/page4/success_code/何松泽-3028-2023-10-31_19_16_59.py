n,m,l = map(int,input().split(','))
d = []
for x in range(m):
    p = n + l*x
    d.append(p)
print(d)
