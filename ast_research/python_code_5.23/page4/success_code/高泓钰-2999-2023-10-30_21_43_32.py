a=list(input().split())
b,c=map(int,input().split())
eval=a[b]
a[b]=a[c]
a[c]=eval
print(a)
