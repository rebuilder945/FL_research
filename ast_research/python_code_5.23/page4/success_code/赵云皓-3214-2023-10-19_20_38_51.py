a=eval(input())
b=[]
c=[]
for x in a:
    if x!=0:
        b.append(x)
    else:
        c.append(x)
d=b+c
print(d)
