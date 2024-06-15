a=list()
b,c=eval(input())
d=a.copy()
d[b]=a[c]
d[c]=a[b]
print(d)
