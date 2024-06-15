ls = eval(input())
ls2 = [x for x in ls if ls.count(x) == 1]
if len(ls2) == 0:
    print('False')
else:
    ls2.sort()
    print(ls2)
