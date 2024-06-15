def sushu(n):
    if n>=2:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    else:
        return False  
# print(sushu(2))
lst=eval(input())
lst2=[]
for i in range(len(lst)):
    if sushu(lst[i]):
        lst2.append(lst[i])
print(lst2)

