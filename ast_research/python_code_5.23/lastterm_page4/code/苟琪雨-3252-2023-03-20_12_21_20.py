def Fibnacci(num，n):
    if n==1 or n==0:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


