def Fibonacci(n)
    a, b = 1, 1
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


