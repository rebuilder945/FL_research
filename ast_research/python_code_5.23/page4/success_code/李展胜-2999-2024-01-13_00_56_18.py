a=eval(input())
b,c=int,input().split()
d=a.copy()
d[b]=a[c]
d[c]=a[b]
print(d)
