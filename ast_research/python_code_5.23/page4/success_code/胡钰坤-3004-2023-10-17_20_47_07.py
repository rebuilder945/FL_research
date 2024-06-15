def sushu(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True
n = eval(input())
ls = []
for i in n:
    if i >= 2:
        if sushu(i):
            ls.append(i)
        i += 1
print(ls)
       



