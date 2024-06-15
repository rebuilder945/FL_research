ls=eval(input())
ls1=ls[::-1]
ls2=[]
for x in ls1:
    if x in ls2:
        continue
    else:
        ls2.append(x)
ls3=ls2[::-1]
print(ls3)
