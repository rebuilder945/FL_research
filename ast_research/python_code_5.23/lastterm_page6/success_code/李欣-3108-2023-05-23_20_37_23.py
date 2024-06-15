ls1=eval(input())
ls2=''.join(ls1)
ls3=[]
for m in ls2:
    if m not in ls3:
        ls3.append(m)
for i in ls3:
    s=ls2.count(i)
    print('%s,%d'%(i,s))
