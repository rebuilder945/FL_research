a = eval(input())
c = []
for i in a[-1::-1]:
    if i not in c:
        c.append(i)
reversed(c)
print(c)
