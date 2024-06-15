def Fibonacci(num,n):
        a=num[0],b=num[1]
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        return c





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


