a=eval(input())
b,c=map(int,input().split())
d=a.copy()
d[b]=a[c]
d[c]=a[b]
print(a)
