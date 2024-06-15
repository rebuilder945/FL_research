a=eval(input())
b=[]
c=[]
for i in a:
    if i==0:
        b.append(i)
for x in a:
    if x!=0:
        c.append(x)
print(c+b)

