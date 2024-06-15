a=list(map(str,input().split()))
b,c=map(int,input().split())
d=a.copy()
a[b]=a[c]
d[c]=a[b]
print[d]
