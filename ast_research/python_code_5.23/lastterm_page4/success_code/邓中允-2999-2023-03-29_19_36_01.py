a=input().split()
b,c=map(int,input().split())
temp=a[b]
a[b]=a[c]
a[c]=temp
print(a)
