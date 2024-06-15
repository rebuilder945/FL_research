a = eval(input())
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b[0])
