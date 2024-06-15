n,m,l=eval(input())
a=[]
b=n
a.append(n)
for x in range(m-1):
    b+=l
    a.append(b)
print(a)

