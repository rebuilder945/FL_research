a=list(input().split())
b,c=map(int,input().split())
d=a[b]
a[b]=a[c]
a[c]=d
print(a)

