def sushu(n):
    if n>=2:
        for i in range(2,n):
            if n%i == 0:
                return
        else:
            return n
    else:
        return

lst=eval(input())
lst2=[]
for n in lst:
    if sushu(n):
        lst2.append(n)
print(lst2)

