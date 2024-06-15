n,m,l = input().split(",")
n = int(n)
m = int(m)
l = int(l)
M = (m-1)*l+n+1
print(list(range(n,M,l)))
