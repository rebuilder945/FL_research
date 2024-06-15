a=input().split()
m=input().split()
b,c=m
b=int(b)
c=int(c)
a[b],a[c] = a[c],a[b]
print(a)
