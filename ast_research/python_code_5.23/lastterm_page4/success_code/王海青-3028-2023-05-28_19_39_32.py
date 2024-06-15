n,m,l=input().split(',')
n=int(n)
m=int(m)
l=int(l)
k=n+(m-1)*l
f=list(range(n,k+1,l))
print(f)
