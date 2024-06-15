def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
lst=eval(input())
lst1=[]
for x in lst:
    if sushu(x):
        lst1.append(x)
print(lst1)
