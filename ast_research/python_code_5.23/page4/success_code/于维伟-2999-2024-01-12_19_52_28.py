a=list(map(str,input().split()))
n,m=int(input())
d=a.copy
d[n]=a[m]
d[m]=a[n]
print(d)
