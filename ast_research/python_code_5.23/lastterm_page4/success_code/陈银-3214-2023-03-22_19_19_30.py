a = eval(input())
b = a.count(0)
for x in a:
    if x == 0:
        a.remove(0)
        a.append(0)
print(a)
