a=eval(input())
b=[]
c=[]
for x in a:
    for y in range(2,x):
        if x%y==0:
            b.append(x)
for i in a:
    if i not in b:
        c.append(i)
print(c)

