a=eval(input())
b=[]
for i in range(a+1):
    b.append(i)
del b[0]
c=b[0]
del b[0]
b.append(c)
print(b)
