def Fibonacci(num,n):

        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


