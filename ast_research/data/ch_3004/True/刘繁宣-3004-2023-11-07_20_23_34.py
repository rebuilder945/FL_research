def sushu(n):
    if n > 1 :
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    else:
        return False
ls=eval(input())
ls1=[]
for i in range(len(ls)):
    if sushu(ls[i]):
        ls1.append(ls[i])
print(ls1)
