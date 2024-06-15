ls = eval(input())
ls2 = [x for x in ls if x > 1]
ls3 = []
for x in ls2:
    for i in range(2,x):
        if x%i == 0:
            ls3.append(x)
ls2 = [x for x in ls2 if x not in ls3]
print(ls2)
