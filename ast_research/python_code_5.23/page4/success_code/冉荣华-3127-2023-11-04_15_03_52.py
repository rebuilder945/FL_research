n=eval(input())
a=list(range(1,n+1))
b=a.copy()
for i in range(n-1):
    b[i]=a[i+1]
b[n-1]=a[0]
print(b)
