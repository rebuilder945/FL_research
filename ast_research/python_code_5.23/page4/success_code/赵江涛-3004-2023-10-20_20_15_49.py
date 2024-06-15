def jarge(x):
    for i in range(3,x):
        if x%i == 0:
            break
    return 0





ls = eval(input())
ls2 = []
for x in ls:
    if jarge(x) == 0:
        ls2.remove(x)
print(ls2)
