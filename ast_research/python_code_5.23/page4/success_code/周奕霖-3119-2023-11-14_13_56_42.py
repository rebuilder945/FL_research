a = eval(input())
b = a[::-1]
c = []
for i in range(len(a)):
    if b[i] in c:
        pass
    else:
        c.append(b[i])
print(c)
