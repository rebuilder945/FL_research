n = eval(input())
ls = []
ls1 = []
for i in n:
    if i != 0:
        ls.append(i)
    else:
        ls1.append(i)
ls2 = ls + ls1
print(ls2)

