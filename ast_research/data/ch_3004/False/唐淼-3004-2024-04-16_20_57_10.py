def sushu(n):
    if n >=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
            else:
                return True
lst=eval(input())
lst1=[]
for i in lst:
    if bool(sushu(i))==True:
        lst1.append(i)
    else:
        pass
print(lst1)

