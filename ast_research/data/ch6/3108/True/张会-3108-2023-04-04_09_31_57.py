ls = eval(input())
ls1 =[]
ls2 =[]
for i in ls:
    for x in i:
        ls1.append(x)
ls1.sort()
for x in ls1:
    if x not in ls2:
        ls2.append(x)
ls3 = []
for m in ls2:
    if m in ls1:
        a = ls1.count(m)
        ls3.append(a)
for n in range(len(ls2)):
    print("%s,%s"%(ls2[n],ls3[n]))

