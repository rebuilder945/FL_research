a=eval(input())
b=[]
c=[]
for i in a:
    if i!=0:
        b.append(i)
for j in a:
    if j==0:
        c.append(j)
print(b+c)
