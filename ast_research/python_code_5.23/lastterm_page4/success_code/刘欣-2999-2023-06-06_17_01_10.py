lis=list(input().split())
n,m=input().split()
n=int(n)
m=int(m)
lis[n],lis[m]=lis[m],lis[n]
print(lis)
