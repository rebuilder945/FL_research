n=eval(input())
ls=[]
ls1=[]
for i in n:
    ls2=list(i)
    ls1=ls1+ls2
for x in ls1:
    if x not in ls:
        ls.append(x)
ls.sort()
for y in ls:
    a=ls1.count(y)
    ls3=[str(y),str(a)]
    print(",".join(ls3))
