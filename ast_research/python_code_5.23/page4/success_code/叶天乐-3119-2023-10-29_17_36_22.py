ls1 = eval(input())
ls2 =ls1[::-1]
ls3 = []
for i in ls2:
    if i not in ls3:
        ls3.append(i)
print(ls3)
