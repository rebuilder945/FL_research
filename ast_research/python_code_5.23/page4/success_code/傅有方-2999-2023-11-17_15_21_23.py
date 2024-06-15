a=map(str,input().split())
a=list(a)
b,c=map(int,input().split())
d=a.copy
d[c]=a[b]
d[b]=a[c]
print(d)
