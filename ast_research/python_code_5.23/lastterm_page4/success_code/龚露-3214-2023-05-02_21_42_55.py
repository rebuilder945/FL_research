ls = eval(input())
ls1 = ls.copy()
for x in ls:
    if x ==0:
        ls1.remove(x)
        ls1.append(0)
print(ls1)


