a = eval(input())
c = []
for x in a.reverse():
    if x not in c:
        c.append(x)
print(c)
