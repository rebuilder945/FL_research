def sushu(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
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
