x = eval(input())
d = {}
for i in x:
    for k in i:
        if k not in d :
            d[k] = 1
        else:
            d[k] += 1
for i in sorted(d.keys()):
    print('%s,%d'%(i,d[i]))

