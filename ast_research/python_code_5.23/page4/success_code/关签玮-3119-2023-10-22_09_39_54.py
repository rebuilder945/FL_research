ls1=eval(input())
ls2=ls1.copy()
for i in ls1:
    a=ls2.count(i)
    if a!=1:
        ls2.remove(i)
print(ls2)
