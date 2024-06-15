a=eval(input())
b=[i+1 for i in range(a)]
c=[]
for i in range(len(b)):
    c.append(b[i-1])
print(c)
