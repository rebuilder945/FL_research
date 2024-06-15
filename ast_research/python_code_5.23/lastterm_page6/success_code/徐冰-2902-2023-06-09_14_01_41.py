def sushu(x):
    if x==2:
        return True
    elif x>2:
        for i in range(2,x//2+1):
            if x%i==0:
                return False
        return True
    else:
        return False
ls=eval(input())
ls1=[]
for i in ls:
    if sushu(i):
        ls1.append(i)
print(ls1)
