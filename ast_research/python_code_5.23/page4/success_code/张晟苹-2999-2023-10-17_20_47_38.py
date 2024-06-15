from posixpath import split


a=input().split(' ')
b,c=input().split()
a[b],a[c]=a[c],a[b]
print(a)
