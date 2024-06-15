n,m,l=eval(input())
a=n
b=[n]
for x in range (m-1):
    a=a+l
    b.append(a)
print(b)
