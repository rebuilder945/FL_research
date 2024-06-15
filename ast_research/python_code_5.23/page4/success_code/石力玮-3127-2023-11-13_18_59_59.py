a=eval(input())
b=list(range(a+1))
c=b.copy()
for x in range(a-1):
    c[x]=b[x+1]
c[a-1]=b[0]
print(c)

