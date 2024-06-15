ls1 = eval(input())
ls2 = []
for x in ls1:
    ls2 = ls2 + list(x)
ls2.sort()
ls3 = []
for x in ls2:
    if x not in ls3:
        ls3.append(x)
for x in ls3:
    ls4 = []
    ls4 = [x,str(ls2.count(x))]
    print(",".join(ls4))
    

