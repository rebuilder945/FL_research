ls1=eval(input())
ls2=[]
ls3=[]
for x in ls1:
    for i in range(2,x):
        if x%i==0:
            ls2.append(x)
            break
        else:
            ls3.append(x)
print(ls3)
