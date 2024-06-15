ls1=eval(input())
ls2=ls1.copy()
for i in ls1:
    if i==0:
        ls2.remove(0)
        ls2.append(0)
    if i!=0:
        pass
print(ls2)
