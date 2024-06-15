c=eval(input())
c1=c.copy()
for x in c1:
    if c.count(x)>1:
        c.remove(x)
print(c)
