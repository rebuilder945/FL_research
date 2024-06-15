n,m,l=eval(input())
x1=[n]
x2=n
for i in range(m-1):
    x2+=l
    x1.append(x2)
print(x1)
