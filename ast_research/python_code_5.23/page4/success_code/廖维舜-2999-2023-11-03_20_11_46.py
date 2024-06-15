a=list(map(str,input().split()))
b,c=eval(input())
d=a.copy()
d[b]=a[c]
d[c]=a[b]
print(d)
