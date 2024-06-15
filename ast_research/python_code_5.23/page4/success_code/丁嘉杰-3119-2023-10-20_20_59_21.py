ls1=eval(input())
for i in range(len(ls1)):
    if ls1[i]==True and type(ls1[i])==bool:
        ls1[i]=str(ls1[i])
ls2=ls1.copy()
for i in ls2:
    if ls1.count(i)!=1:
        ls1.remove(i)
        for i in range(len(ls1)):
            if ls1[i]=='True':
                ls1[i]=eval(ls1[i])
print(ls1)
