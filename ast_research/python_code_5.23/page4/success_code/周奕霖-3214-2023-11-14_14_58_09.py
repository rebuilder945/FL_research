a = eval(input())
for x in a:
    if x == 0:
        a.append(x)
        del x
print(a)

