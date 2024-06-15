n,m,l=eval(input())
ls=[n]
for i in range(m-1):
    n+=l
    ls.append(n)
print(ls)
