def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
lst=eval(input())
a=[]
if 1 in lst:
    for x in lst:
        if sushu(x):
            a.append(x)
    a.insert(0,1)
else:
    for x in lst:
        if sushu(x):
            a.append(x)
print(a)

