def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
lst=eval(input())
lst1=[]
for i in lst:
    if sushu(i):
        lst1.append(i)
lst1.remove(0)
lst1.remove(1)
print(lst1)
