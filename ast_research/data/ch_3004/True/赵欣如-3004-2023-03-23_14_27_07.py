ls1=eval(input())
ls2=ls1.copy()
for x in ls1:
    if x==0 or x==1:
        ls2.remove(x)
    for i in range(2,x):
        if x %i==0:
            ls2.remove(x)
        if ls2.count(x)==0:
            break
print(ls2)
