A=input().split()
n,m=input().split()
ls=list(A)
n=int(n)
m=int(m)
ls[n],ls[m]=ls[m],ls[n]
print(ls)
