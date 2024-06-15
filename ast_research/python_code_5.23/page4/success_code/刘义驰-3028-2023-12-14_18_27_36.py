n,m,l = map(int,input().split(','))
d = []
for x in range(m):
    k = n+l*x
    d.append(k)
print(d)
