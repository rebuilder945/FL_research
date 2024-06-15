a=input().split()
n,m=map(int,input().split())
c=a[m]
a[m]=a[n]
a[n]=c
print(a)
