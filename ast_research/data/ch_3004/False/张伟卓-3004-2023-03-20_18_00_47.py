def sushu(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n>2:
        for i in range (2,n):
            if n % i ==0:
                return False
            return True
ls1=eval(input())
ls2=[]
for num in ls1:
    if sushu(num):
        ls2.append(num)
print(ls2)
