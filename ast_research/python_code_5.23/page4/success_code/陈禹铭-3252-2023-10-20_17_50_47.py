def Fibonacci(n):
    fib = [0] * (n + 1)  
    fib[1] = 1  
    fib[2] = 1  
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]  
    return fib[n]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


