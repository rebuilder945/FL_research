a=input().split()
e=input().split()
b=int(e[0])
c=int(e[1])
d=a[b]
a[b]=a[c]
a[c]=d
print(a)
