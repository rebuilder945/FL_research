a=eval(input())
b=[]
c=[]
for x in a:
    for i in range(2,x):
            c.append(x%i)
    if c.count(0)==0:
        b.append(x)
    c=[]
print(b)
