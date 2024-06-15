ls = eval(input())
ls1 = []
ls2 = []
for i in ls:
    if i > 0:
        ls1.append(i)
    else:
        ls2.append(i)
print(ls1+ls2)


