a = input().split()
ls = list(a)
n,m = map(int,input().split())
g=ls[n]
h=ls[m]
ls[n]=h
ls[m]=g
print(ls)
