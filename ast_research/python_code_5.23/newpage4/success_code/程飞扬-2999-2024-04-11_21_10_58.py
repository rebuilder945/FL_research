a=input().split()
n,m=input().split()
c=list(a)
c[int(n)],c[int(m)]=c[int(m)],c[int(n)]
print(c)
