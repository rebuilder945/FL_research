n,m,l=eval(input())
a=[n]
for i in range(m-1):
    b=a[-1]+l
    a.append(b)
print(a)
