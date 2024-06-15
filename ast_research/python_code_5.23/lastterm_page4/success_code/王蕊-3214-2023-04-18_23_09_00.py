ls1=eval(input())
a=ls1.count(0)
c=0
i=0
if 0 in ls1:
    while c<a:
        c+=1
        ls1.remove(0)
        ls2=ls1.copy()
        while i <a:
            i+=1
            ls2.append(0)
    print(ls2)
else:
    print(ls1)

