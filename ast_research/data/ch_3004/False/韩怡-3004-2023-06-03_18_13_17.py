def sushu(n):
    if n>=2:
        for i in range(2,n):
            if n%i == 0:
                pass
        else:
            return n
    else:
        pass

lst=eval(input())
lst2=[]
for n in lst:
    if sushu(n):
        lst2.append(n)
print(lst2)

