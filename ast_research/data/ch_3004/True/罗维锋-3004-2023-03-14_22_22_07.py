a=eval(input())
b=[]
c=[]
for x in a:
    for i in range(1,x+1):
        if (x%i)==0:
            c.append(i)
    if len(c)==2:
        b.append(x)
    c=[]
print(b)

