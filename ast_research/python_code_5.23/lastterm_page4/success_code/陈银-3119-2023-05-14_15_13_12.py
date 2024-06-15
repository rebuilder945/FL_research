a = eval(input())
a.reverse()
print(a)
c = []
for x in a:
    if x not in c:
        c.insert(0,x)
print(c)


