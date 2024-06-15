def sushu(n):
    if n>=2:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
                return True
    else:
        return True
lst=eval(input())
lst1=[]
for x in lst:
    if(sushu(x)):
        lst1.append(x)
print(lst1)


