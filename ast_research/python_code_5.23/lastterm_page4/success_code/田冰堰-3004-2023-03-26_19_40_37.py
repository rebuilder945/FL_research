def sushu(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True
n = eval(input())
for i in range(2,n):
    print(i,end='')
