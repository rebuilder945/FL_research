ls1=eval(input())
ls2=ls1.copy()
for x in ls1:
    for i in range(2,x):
        if x%i==0:
            ls2.remove(x)
        else:
            continue
print(ls2)        
