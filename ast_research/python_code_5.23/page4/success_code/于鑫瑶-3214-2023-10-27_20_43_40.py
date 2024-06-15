ls1=eval(input())
ls2=[]
ls3=[]
for i in ls1:
    if i==0:
       ls2.append(i)
    else:
        ls3.append(i)
ls3.extend(ls2)
print(ls3)


