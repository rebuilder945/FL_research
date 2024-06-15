def sushu(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
ls1=[]        
ls=eval(input())
for x in ls:
    if sushu(x):
        ls1.append(x)
print(ls1)
