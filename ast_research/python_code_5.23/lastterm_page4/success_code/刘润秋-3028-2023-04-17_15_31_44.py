n,m,l=map(int,input().split(','))
ls=[]
for x in range(m):
    x=n+l*x
    ls.append(x)
print(ls)
