ls = eval(input())
ls2 = [x for x in ls if x > 1]
for x in ls2:
    for i in range(2,x):
        if x%i == 0:
            ls2.remove(x)
print(ls2)
