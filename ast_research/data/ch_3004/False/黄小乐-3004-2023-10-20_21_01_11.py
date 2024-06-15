ls = list(eval(input()))
ls2 = []
for x in ls:
    for i in range(2,x):
        if x%i == 0:
            ls2.append(x)
ls3 = []
for b in ls2:
    for a in ls:
        if a not in ls2:
            ls3.append(a)
print(ls3)

    


