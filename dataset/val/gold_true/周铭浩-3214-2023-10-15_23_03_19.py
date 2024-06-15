ls1=eval(input())
ls3=ls1.copy()
ls2=[]
for x in ls1:
    if x==0:
        ls2.append(x)
        ls3.remove(0)
    else:
        continue
ls4=ls3+ls2
print(ls4)
