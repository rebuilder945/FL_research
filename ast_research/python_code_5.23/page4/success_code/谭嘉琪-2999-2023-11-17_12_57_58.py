a=input().split()
n,m=map(int,input().split())
b=a[n]
c=a[m]
a[n],a[m]=c,b
print(a)

