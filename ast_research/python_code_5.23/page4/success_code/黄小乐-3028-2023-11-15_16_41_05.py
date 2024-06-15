n,m,l=input().split(",")
n=int(n)
m=int(m)
l=int(l)
ls=[]
for i in range(0,m):
    s=n+i*l
    ls.append(s)
print(ls)

