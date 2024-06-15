ls = eval(input())
ls2 = ls[::-1]
ls3 = []
for x in ls2:
    if x not in ls3:
        ls3.append(x)
ls4 = ls3[::-1]
print(ls4)

