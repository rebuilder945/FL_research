a=list(map(str,input().split(' ')))
n,m=map(int,input().split())
b=a.copy()
b[n]=a[m]
b[m]=a[n]
print(b)
