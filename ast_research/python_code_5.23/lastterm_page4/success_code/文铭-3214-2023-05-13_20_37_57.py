ls = eval(input())
ls1 = []
for x in ls:
    if x != 0:
        ls1.append(x)
for x in ls:
    if x == 0:
        ls1.append(x)
print(ls1)
