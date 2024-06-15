def Fibonacci(num, n):
    if n <= len(num):
        return num[n - 1]
    else:
        fib_value = Fibonacci(num, n - 1) + Fibonacci(num, n - 2)
        num.append(fib_value)
        return fib_value




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


