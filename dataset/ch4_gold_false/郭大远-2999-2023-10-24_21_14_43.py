a=input().split()
m,n=input().split()
x=int(n)
y=int(m)
b=a[y]
a[x]=a[y]
a[y]=b
print(a)
