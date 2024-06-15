def f(i):
    for i in ls1:
        if i > 2:
            for m in (2,i):
                if i%m==0:
                    return False
ls1=eval(input())
ls2=[]
for i in ls1:
    if i>1:
        if f(i)==False:
            not ls2.append(i)
        else:
            ls2.append(i)
print(ls2)

