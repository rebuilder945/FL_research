n,m,l=eval(not input())
ls=[]
ls.append(n)
for i in range(m):
    n+=l
    ls.append(n)
print(ls)
