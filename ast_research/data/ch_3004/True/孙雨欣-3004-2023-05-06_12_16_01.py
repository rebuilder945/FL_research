def sushu(n):
    f=True
    if n==1 or n==0:
        f=False
    else:
        for i in range(2,n//2+1):
            if n %i==0:
                f=False
                break
    return f  
ls1=eval(input())
ls2=[]
for i in ls1:
    if sushu(i):
        ls2.append(i)
print(ls2)
