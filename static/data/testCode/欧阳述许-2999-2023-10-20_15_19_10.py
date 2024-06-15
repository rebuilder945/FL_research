a=input().split()
b,c=map(input().split())
a[b]=a[c]
a[c]=a[b]
print(a)
