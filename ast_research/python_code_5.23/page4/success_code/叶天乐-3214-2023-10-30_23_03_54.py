ls1 = eval(input())
ls2 = []
for i in ls1:
    if i != 0:
        ls2.append(i)
        for m in ls1:
            if m not in ls2:
                ls2.append(m)
print(ls2)
