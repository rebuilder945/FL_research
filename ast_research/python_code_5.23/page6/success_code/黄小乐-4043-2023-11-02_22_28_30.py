ls=eval(input())
ls.sort()
ls1=[]
ls2=[]
ls3=[]
for x in ls:
    for i in x:
        if i not in ls1:
            ls1.append(i)
for x in ls:
    for i in x:
        ls2.append(i)
for x in range(len(ls2)):
    if x==0:
        n=ls2.count(ls2[0])
        ls3.append(n)
    elif x>0:
        if ls2[x]!=ls2[x-1]:
            n=ls2.count(ls2[x])
            ls3.append(n)
for i in range(len(ls3)):
    print("%s,%d"%(ls1[i],ls3[i]))

