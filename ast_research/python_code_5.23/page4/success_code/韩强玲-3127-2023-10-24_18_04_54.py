n = eval(input())
b = list(range(1,n+1))
c = b.copy()
for y in range (n-1):
     c[y]=b[y+1]
c[n-1]=b[0]
print(c)

