a=eval(input())
b=[i+1 for i in range(a)]
c=b.copy()
d=[]
for i in range(len(c)-1):
    c.append(b[i+1])
c.append(b[0])
print(c)
