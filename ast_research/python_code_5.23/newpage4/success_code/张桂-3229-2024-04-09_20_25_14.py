ls = eval(input())
ls2 = []
for i in ls:
    if ls.count(i) == 1:
        ls2.append(i)
ls2.sort(reverse=False)
if len(ls2) > 0:
    ls1 =','.join(str(a) for a in ls2)
    print(ls1)
else:
    print("False")

