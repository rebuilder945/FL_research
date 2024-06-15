n,m,l=eval(input())
ls=[n]
b=n
for i in range(m-1):
    b=b+l
    ls.append(b)
print(ls)
