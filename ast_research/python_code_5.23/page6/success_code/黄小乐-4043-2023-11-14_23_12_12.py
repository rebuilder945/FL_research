a=eval(input())
ls1=[]
ls2=[]
ls3=[]
for x in a:
    for i in x:
        if i not in ls1:
            ls1.append(i)
for x in a:
    for i in x:
        ls2.append(i)
ls1.sort()
ls2.sort()
for i in range(len(ls2)):
    if i==0:
        n=ls2.count(ls2[0])
        ls3.append(n)
    elif i>0:
        if ls2[i]!=ls2[i-1]:
            n=ls2.count(ls2[i])
            ls3.append(n)
for i in range(len(ls1)):
    print("%s,%d"%(ls1[i],ls3[i]))





