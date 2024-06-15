ls1=eval(input())
a=ls1.count(0)
if 0 in ls1:
    ls1.remove(0)
    ls2=ls1.copy()
    i=0
    while i <a:
        i+=1
        ls2.append(0)
    print(ls2)
else:
    print(ls1)

