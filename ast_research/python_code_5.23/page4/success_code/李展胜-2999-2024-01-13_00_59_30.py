a=list(str,input().split())
b,c=int,input().split()
d=a.copy()
d[b]=a[c]
d[c]=a[b]
print(d)
