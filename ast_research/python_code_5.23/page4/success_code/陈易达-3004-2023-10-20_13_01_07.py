ls = eval(input())
ls2 = []
for x in ls:
    for i in range(2,x):
        if x%i:
            ls2.append(x)
ls3 = []
for x in ls2:
    if x not in ls3:
        ls3.append(x)
if 2 in ls:
    ls3.insert(0,2)
print(ls3)

