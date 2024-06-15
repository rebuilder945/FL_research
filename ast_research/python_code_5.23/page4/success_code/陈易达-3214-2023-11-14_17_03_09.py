ls = eval(input())
ls2 = []
for x in ls:
    if x != 0:
        ls2.append(x)
n = len(ls)-len(ls2)
for x in range(n):
    ls2.append(0)
print(ls2)
