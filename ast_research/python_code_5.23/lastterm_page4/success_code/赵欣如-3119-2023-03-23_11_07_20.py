ls=eval(input())
ls2=ls.copy()
for i in ls:
    if ls2.count(i)>1:
        ls2.remove(i)
    if ls.count(i)==1:
        pass
print(ls2)
