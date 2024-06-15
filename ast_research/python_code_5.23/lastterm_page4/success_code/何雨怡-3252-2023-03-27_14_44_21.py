def Fibonacci(num,n):
    if n==1 or n==2:
        return 1
    if n==0:
        return 0
    return Fibonacci(num,n-1)+Fibonacci(num,n-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


