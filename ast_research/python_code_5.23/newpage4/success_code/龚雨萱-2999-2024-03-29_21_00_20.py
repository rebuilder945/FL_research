ls=list(input().split())
n,m=input().split()
n=int(n)
m=int(m)
ls[n],ls[m]=ls[m],ls[n]
print(ls)
