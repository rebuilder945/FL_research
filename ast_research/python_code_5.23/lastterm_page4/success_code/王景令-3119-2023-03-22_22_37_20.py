a = eval(input())
c = []
for i in a[-1::-1]:
    if i not in c:
        c.append(i)
d = list(reversed(c))
print(d)
