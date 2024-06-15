ls = list(eval(input()))
ls2 = []
for x in ls:
    if x != 0:
        ls2.append(x)
n = ls.count(0)
for i in range (n):
    ls2.append(0)
print(ls2)


