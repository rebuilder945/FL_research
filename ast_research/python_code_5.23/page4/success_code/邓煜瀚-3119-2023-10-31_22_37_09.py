a=eval(input())
c=a.copy()
for i in a:
    if a.count(i)>=2:
        for i in range(a.count(i)-1):
            c.append(i)
print(c)

