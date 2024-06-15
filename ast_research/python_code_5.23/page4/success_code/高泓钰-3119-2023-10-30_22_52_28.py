ls=eval(input())
ls2=ls[:]
for i in ls:
    x=ls2.count(i)
    if x>1:
        ls2.remove(i)
print(ls2)
