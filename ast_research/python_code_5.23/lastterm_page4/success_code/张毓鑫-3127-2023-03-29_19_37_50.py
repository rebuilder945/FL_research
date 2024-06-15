a=eval(input())
b=[]
for i in range(a):
    b.append(i)
c=b[1]
del b[1]
b.append(c)
print(b)
