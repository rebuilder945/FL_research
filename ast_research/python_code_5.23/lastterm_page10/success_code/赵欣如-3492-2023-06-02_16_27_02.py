ls=str(input())

if len(ls)>=1:
    ls1=[]
    for i in ls:
        ls1.append(ls.count(i))
    for x in ls1:
        if x==1:
            print(ls[ls1.index(x)])
            break
else:
    print("None")
