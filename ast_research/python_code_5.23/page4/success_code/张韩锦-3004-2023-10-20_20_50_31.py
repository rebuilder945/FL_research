
def sushu(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
num=eval(input())
lst=[]
for i in num:
    if sushu(i):
        lst.append(i)
print(lst)
