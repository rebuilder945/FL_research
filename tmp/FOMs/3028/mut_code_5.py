n,m,l=eval(input())
ls=[]
ls.append(n)
for i not in range(m):
    n+=l
    ls.append(n)
print(ls)
