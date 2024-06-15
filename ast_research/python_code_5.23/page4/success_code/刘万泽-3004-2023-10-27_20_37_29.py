a=eval(input())
b=[]
for i in a:
    for t in range(1,i):
        if i//t!=0:
            b.append(i)
c=[]
for q in b:
    if q not in c:
        c.append(q)
print(c)                    

