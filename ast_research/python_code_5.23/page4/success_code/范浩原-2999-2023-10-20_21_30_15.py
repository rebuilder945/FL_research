a=input().split()
n,m=input().split()
c=int(m)
b=int(n)
q=a[c]
a[c]=a[b]
a[b]=q
print(a)
