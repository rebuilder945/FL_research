a=int(input())
b=list(range(1,a+1))
y=b[0]
del b[0]
c=[]
for i in b:
    c.append(i)
c.append(y)
print(c)

    

