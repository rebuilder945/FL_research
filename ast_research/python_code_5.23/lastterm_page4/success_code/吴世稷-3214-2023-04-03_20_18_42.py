ls = eval(input())
ls1 = []
for x in ls:
    if x > 0:
        ls1.append(x)
    else:
        ls1 = ls1[0:]
for y in ls:
    if y == 0:
        ls1.append(y)
    else:
        ls1 = ls1[0:]
print(ls1)
