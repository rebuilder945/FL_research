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
print(ls3)      
