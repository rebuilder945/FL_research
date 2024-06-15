a = eval(input())
b = []
for i in a:
    if i != 0 :
        b.append(i)
    else:
        continue
for i in a:
    if i not in b:
        b.append(i)
print(b)