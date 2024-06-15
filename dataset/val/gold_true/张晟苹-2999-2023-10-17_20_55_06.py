from posixpath import split


a=input().split(' ')
b,c=map(int,input().split())
a[b],a[c]=a[c],a[b]
print(a)
