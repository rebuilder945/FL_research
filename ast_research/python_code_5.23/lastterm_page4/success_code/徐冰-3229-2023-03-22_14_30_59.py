ls1=eval(input())
ls1.sort()
ls2=[]
if (all(ls1.count(m)>1 for m in ls1)):
    print(False)
else:
    for x in ls1:
        if ls1.count(x)==1:
            ls2.append(x)
    ls3=[str(i) for i in ls2]
    print(",".join(ls3))
