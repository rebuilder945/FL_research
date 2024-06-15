ls1 = eval(input())
ls2 = []
for x in ls1:
    if x in ls2:
        continue
    else:
        ls2.append(x)
print(ls2)
