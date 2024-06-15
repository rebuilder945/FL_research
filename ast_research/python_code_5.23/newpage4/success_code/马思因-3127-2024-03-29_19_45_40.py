a=int(input())
b=[i for i in range(1,a+1)]
c=[]
for i in range(1,len(b)):
    c.append(b[i])
c.append(b[0])
print(c)
