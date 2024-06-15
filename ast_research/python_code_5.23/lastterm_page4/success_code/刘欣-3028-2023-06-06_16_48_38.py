n,m,l=input().split(",")
m=int(m)
n=int(n)
l=int(l)
lis=[]
for i in range(m):
    i=int(i)
    lis.append(n)
    n += l
print(lis)
