n,m,l=input().split(',')
n=eval(n)
m=eval(m)
l=eval(l)
ls=[]
for i in range(m):
    ls.append(n)
    n=n+l
print(ls)

