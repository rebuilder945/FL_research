ls = eval(input())
ls1 = []
ls2 = list(reversed(ls))
for x in ls2:
    if x not in ls1:
        ls1.append(x)
    else:
        ls1 = ls1[0:]
ls3 = list(reversed(ls1))
print(ls3)
