ls1=eval(input())
ls2=[]
for i in ls1:
    if i==2:
        ls2.append(i)
    else:
        for m in (2,i):
            if not i%m ==0:
                ls2.append(i)
print(ls2)

