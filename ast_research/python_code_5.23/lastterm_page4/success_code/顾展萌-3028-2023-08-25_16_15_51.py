n,m,l = input().split(",")
n = int(n)
m = int(m)
l = int(l)
M = m*l+n+1
print(list(range(n,M,l)))
