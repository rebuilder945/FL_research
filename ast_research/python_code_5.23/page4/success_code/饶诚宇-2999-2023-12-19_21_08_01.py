a=list(map(str,input().split))
n,m=map(int,input().split())
b=a.copy()
b[n],b[m]=a[m],a[n]
print(b)
