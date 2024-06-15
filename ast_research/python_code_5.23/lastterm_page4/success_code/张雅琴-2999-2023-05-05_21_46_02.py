a=input().split()
b,c=map(int,input().split())
x1=a[b]
a[b]=a[c]
a[c]=x1
print(a)
