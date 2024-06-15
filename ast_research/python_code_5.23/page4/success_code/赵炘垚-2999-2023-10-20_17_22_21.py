a=list(map(str,input().split()))
b,c=map(int,input().split())
d=a.copy()
d[a]=a[c]
d[c]=a[b]
print(d)
