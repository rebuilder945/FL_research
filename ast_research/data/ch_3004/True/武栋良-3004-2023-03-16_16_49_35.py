ls1 = eval(input())
ls2 = []
for x in ls1:
    if x==0:
        continue
    elif x==1:
        continue
    elif x==2:
        ls2.append(2)
    else:
        for i in range(2,x):
            if x%i ==0:
                break
        else:
            ls2.append(x)
print(ls2) 
