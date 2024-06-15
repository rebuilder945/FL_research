def sushu(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
lst1 = eval(input())
lst2 = []
for n in lst1:
   if sushu(n):
        lst2.append(n)
print(lst2)

