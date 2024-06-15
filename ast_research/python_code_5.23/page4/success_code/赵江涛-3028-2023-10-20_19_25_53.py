n,m,d = eval(input())
ls  =[n]
for i in range(m-1):
    n+=d
    ls.append(n)
print(ls)
