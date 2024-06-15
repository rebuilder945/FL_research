ls1=eval(input())
ls2=ls1.copy()
for i in range(len(ls1)):
    if len(ls2)==1:
        print(ls2)
    if len(ls2)>1:
        for x in ls1:
            if ls1.count(x)>1:
                ls2.append(x)
            print(ls2)
