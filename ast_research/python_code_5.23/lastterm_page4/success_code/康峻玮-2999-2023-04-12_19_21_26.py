ls=input().split()
n,m=input().split()
a=int(n)
b=int(m)
c=ls[a]
ls[a]=ls[b]
ls[b]=c
print(ls)


