a = eval(input())
c = []
for i in range(len(a)):
    if a[i] in c:
        pass
    else:
        c.append(a[i])
print(c)
