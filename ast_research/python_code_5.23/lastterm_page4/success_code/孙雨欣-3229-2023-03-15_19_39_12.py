def only(ls1):
    ls2=[]
    for i in ls1:
        if ls1.count(i)==1:
            ls2.append(ls1[i])
            ls2.sort()
    return ls2
ls=eval(input())
ls3=only(ls)
if ls3==[]:
    print(False)
else:
    print(*ls3,sep=",")
