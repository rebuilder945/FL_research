a=list(input().split())
n,m=map(int,(input().split()))
e=a[n]
r=a[m]
a[m]=e
a[n]=r
print(a)

