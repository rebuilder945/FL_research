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
if 1 in lst1:
    lst1.remove(0)
if 0 in lst1:
    lst1.remove(1)
print(lst1)
