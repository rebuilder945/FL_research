ls1 = eval(input())
ls1.reverse()
ls2 = []
for x in ls1:
    if x not in ls2:
        ls2.append(x)
ls2.reverse()
print(ls2)

