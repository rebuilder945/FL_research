a=list(map(str,input().split()))
n,m=map(int,input().split())
d=a.copy
d[n]=a[m]
d[m]=a[n]
print(d)
