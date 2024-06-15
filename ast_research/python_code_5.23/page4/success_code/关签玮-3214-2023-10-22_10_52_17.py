ls1=eval(input())
ls2=ls1.copy()
ls3=[]
for i in ls1:
    if i==0:
        ls2.remove(i)
        ls3.append(i)
print(ls2+ls3)
