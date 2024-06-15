n,m,l=eval(input())
ls1=[n]
for i in range(m-1):
    x=n+l
    n=x
    ls1.append(n)
print(ls1)

