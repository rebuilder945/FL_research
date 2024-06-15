x=list(map(str,input().split()))
n,m=map(int,input().split())
d=x.copy()
d[n]=x[m]
d[m]=x[n]
print(d)

