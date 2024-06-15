def sushu(n):
    if n>2:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
lst=eval(input())
lst1=[]
for i in lst:
    if sushu(i):
        lst1.append(i)

print(lst1)
