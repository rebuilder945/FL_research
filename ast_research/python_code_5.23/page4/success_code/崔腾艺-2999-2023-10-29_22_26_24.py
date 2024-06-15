a=input().split(" ")
b=input().split(" ")
c=int(b[0])
d=int(b[1])
e=a[c]
f=a[d]
a[c]=f
a[d]=e
print(a)
