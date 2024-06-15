a=eval(input())
c=[]
for x in a:
    c.append(x)
for x in a:
    b=a.count(x)
    if b>=2:
        for y in range(b-1):
            c.remove(x)
    else:
        continue
print(c)


