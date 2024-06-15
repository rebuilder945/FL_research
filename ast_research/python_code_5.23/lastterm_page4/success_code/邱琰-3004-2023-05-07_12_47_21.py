def sushu(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
ls=eval(input())
lst=[]
for i in ls:
    if sushu(i):
        lst.append(i)
    print(lst)

