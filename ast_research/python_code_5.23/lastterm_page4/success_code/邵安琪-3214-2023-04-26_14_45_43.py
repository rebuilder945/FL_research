lst=eval(input())
b=[]
c=[]
for x in lst:
    if x==0:
        b.append(0)
    else:
        c.append(x)
print(c+b)
