ls = eval(input())
one = "".join(map(str,ls))
ls2 = []
for x in one:
    if x not in ls2:
        ls2.append(x)
ls3 = sorted(ls2)
for x in ls3:
    print("%s,%d"%(x,one.count(x)))
