a = eval(input())
a.reverse()
c = ['']
for x in a:
    if x not in c:
        c.insert(0,x)
c.pop()
print(c)

