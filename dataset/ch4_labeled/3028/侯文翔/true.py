n,m,l=eval(input())
ls=[]
ls.append(n)
for i in range(m-1):
    n+=l
    ls.append(n)
print(ls)
