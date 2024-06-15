n=int(input())
a=list(i for i in range(1,n+1))
b=a.copy()
for x in range(n-1):
    b[x]=a[x+1]
    b[n-1]=a[0]
print(b)

