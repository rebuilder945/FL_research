def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
    return True
ls1=eval(input())
ls2=[]
for x in ls1:
    if sushu(x)==True:
        ls2.append(x)
for i in ls2:
    if i==0:
        ls2.remove(i)
    else:
        if i==1:
            ls2.remove(i)
print(ls2)


