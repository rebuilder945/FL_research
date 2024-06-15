ls1=eval(input())
ls2=[]
for x in ls1:
    x=int(x)
    if x==2:
        ls2.append(2)
    else:
        a=0
        for i in range(2,x):
            if x%i==0:
                break
            else:
                a+=1
        if a==x-2:
            ls2.append(x)
        else:
            pass
print(ls2)
