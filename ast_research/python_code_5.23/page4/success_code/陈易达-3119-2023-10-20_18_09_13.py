ls = eval(input())
ls = ls[::-1]
ls2 = []
for x in ls:
    if x not in ls2:
        ls2.append(x)
print(ls2)
