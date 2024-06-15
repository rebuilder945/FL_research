def sushu(n):
    for i in range(1,n//2+1):
        if n%i==0:
            return False
    return True
lst=eval(input())
a=[]
for x in lst:
    if sushu(x):
        a.append(x)
print(a)

