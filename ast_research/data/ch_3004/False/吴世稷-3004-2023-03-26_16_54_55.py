ls = eval(input())
ls1 = []
ls2 = []
ls3 = []
for x in range(len(ls)):
    if ls[x-1] == 2 or ls[x-1] == 3:
        ls1.append(ls[x-1])
    else:
        for i in range(2,ls[x-1]):
            if ls[x-1] % i == 0:
                ls1 = ls1[0:]
            else:
                ls1.append(ls[x-1])
ls2 = sorted(ls1)
for y in ls2:
    if y not in ls3:
        ls3.append(y)
print(ls3)
