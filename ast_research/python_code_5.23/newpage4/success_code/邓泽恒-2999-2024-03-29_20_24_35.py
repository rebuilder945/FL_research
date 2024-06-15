a=input().split()
n,m=map(int,input().split())
t=a[n]
a[n]=a[m]
a[m]=t
print(a)
