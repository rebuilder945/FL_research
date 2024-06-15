a=eval(input())
b=[]
c=[]
for i in a:
    for x in range(1,i):
        if i%x==0:
            c.append(x)
    if len(c)==1:
        b.append(i)
    c=[]
print(b)

