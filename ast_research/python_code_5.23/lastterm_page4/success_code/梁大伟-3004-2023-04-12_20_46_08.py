def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
lst=eval(input())
lst1=[]
for i in lst:
    if sushu(i)==True and i!=1:
        lst1.append(i)
print(lst1)

