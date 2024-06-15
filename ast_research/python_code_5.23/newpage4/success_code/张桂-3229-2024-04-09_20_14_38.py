ls = eval(input())
ls2 = []
for i in ls:
    if ls.count(i) == 1:
        ls2.append(i)
if len(ls2) > 0:
    print(ls2)
else:
    print("False")

