ls = eval(input())
ls2 = []
for x in ls:
    if x == 0:
        ls2.append(x)
while 0 in ls:
    ls.remove(0)
ls3 = ls + ls2
print(ls3)

