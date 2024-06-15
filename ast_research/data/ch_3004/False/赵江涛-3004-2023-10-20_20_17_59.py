def jarge(x):
    for i in range(3,x):
        if x%i == 0:
            return 0





ls = eval(input())
ls2 = []
for x in ls:
    if jarge(x) != 0:
        ls2.append(x)
print(ls2)
