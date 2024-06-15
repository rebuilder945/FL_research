n,m,l=eval(input())
b=[n]
for i in range(m-1):
    n+=l
    b.append(n)
print(b)
