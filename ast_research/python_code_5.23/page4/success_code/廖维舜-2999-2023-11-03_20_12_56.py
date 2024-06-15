a=list(map(str,input().split()))
b,c=int(eval(input()))
d=a.copy()
d[b]=a[c]
d[c]=a[b]
print(d)
