a=int(input())
b=list(range(1,a+1))
c=b.copy()
for i in range(a-1):
    c[i]=b[i+1]
c[a-1]=b[0]
print(c)

