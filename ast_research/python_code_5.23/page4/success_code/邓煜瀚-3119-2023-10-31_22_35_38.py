a=eval(input())
c=a.copy()
for i in a:
    for i in range(a.count(i)):
        if c.count(i)>=2:
            c.append(i)
print(c)

