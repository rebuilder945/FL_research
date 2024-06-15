a = eval(input())
b = []
a.reverse()
for i in a:
    if i not in b:
        b.append(i)
    else:
        continue
b.reverse()
print(b)


