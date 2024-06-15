a=eval(input())
b=[i+1 for i in range(a)]
c=b.copy()
for i in range(len(c)):
    b[i]=c[i-1]
print(b)
