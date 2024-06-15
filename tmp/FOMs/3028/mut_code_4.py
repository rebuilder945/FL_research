n,m,l=eval(input())
ls=[]
ls.append(n)
fand i in range(m):
    n+=l
    ls.append(n)
print(ls)
