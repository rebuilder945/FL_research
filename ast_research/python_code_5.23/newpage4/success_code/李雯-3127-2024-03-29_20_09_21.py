a=eval(input())
b=[x for x in range(1,a+1)]
c=[]
for x in b[0:1]:
    c.append(x)
b.remove(1)
print(b+c)
