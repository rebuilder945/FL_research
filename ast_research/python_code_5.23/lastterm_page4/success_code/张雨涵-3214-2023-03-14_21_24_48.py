ls = eval(input())
ls1 = ls.copy()
h = []
for i in ls:
    if i ==0:
        ls1.pop(ls1.index(i))
        ls1.append(0)
print(ls1)
