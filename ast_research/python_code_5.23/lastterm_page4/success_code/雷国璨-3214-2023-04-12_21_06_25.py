a=eval(input())
b=[]
c=[]
for i in a:
    if i!=0:
        b.append(i)
    else:
        c.append(i)
b.sort()
b.extend(c)
print(b)
