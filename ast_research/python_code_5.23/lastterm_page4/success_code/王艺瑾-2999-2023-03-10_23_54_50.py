a=input().split("")
n,m=input().split("")
b=list(a)
n=int(n)
m=int(m)
b[n],b[m]=b[m],b[n]
print(b)
