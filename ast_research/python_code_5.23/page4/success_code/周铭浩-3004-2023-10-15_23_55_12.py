ls1=eval(input())
ls2=[]
for x in ls1:
    for i in range(2,x):
        if x%i==0:
            ls2.append(x)
        else:
            continue
ls3=[]
for x in ls1:
    if x not in ls2:
        ls3.append(x)
    else:
        continue
ls4=ls3.copy()
for x in ls3:
    if 1 in ls3:
        ls4.remove(1)
    else:
        continue
ls5=ls4.copy()
for x in ls4:
    if 0 in ls4:
        ls5.remove(0)
    else:
        continue
print(ls5)
