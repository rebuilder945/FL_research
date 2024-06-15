ls=eval(input())
ls3=[]
for i in ls:
    ls2=[]
    for x in range(1,i+1,1):
        if i%x==0:
            ls2.append(x)
    if len(ls2)<=2:
        ls3.append(i)
print(ls3)
