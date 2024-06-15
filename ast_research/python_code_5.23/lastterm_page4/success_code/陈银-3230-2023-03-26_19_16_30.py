a = eval(input())
a.sort(reverse = True)
c = []
for x in a:
    if x not in c:
        c.insert(0,x)
        print(c[0],end="")

