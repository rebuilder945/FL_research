n,m,l=map(int,input().split(","))
a=[n]
for i in range(m-1):
    n=n+l
    a.append(n)
print(a)
