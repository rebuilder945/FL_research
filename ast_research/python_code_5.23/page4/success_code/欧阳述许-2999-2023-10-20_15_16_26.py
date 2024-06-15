a=input().split()
b,c=map(input().split)
d=a.copy()
d[b]=a[c]
d[c]=a[b]
print(d)
