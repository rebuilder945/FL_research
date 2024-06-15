def only(ls1):
    ls2=[]
    for i in ls1:
        if ls1.count(i)==1:
            ls2.append(i)
        ls2.sort()
        if ls2==[]:
            print('Flase')
        else:
            print(*ls2,sep=",")
ls=eval(input())
only(ls)
