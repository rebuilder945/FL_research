def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
lst=eval(input())
a=[]
if lst[0]==1:
    for x in lst:
        if sushu(x):
            a.append(x)
    a.remove(1)
else:
    for x in lst:
        if sushu(x):
            a.append(x)
print(a)

