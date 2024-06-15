n,m,l=eval(input())
a=[]
a.append(n)
for i in range(m-1):
    n=n+l
    a.append(n)
print(a)
