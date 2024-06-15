a=eval(input())
b=[]
for i in range(a):
    b.append(i)
c=b[0]
del b[0]
b=b.append(c)
print(b)
