a=eval(input())
c=[]
for x in a:
    if x not in c:
        c.append(x)
for x in c:
    b=a.count(x)
    if b!=1:
        for y in range(b-1):
            a.remove(x)
    else:
        continue
print(a)


