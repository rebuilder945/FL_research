ls1=list(input().split())
n,m=eval(input())
print(n,m)
n=int(n)
m=int(m)
ls1[n],ls1[m]=ls1[m],ls1[n]
print(ls1)

