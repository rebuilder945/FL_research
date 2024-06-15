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
a=set(ls3)
ls4=list(a)
if 1 in ls4:
    ls4.remove(1)
print(ls4)      
