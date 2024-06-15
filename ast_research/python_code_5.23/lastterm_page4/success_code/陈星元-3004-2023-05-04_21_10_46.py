def sushu(x):
    if x==2 or x==3:
        return True
    elif x<=1:
        return False
    else:
        for i in range(2,x//2+1):
            if x%i==0:
                return False
        return True
    
ls=eval(input())
ls2=[]
for x in ls:
    if sushu(x):
        ls2.append(x)
    else:
        continue
print(ls2)

