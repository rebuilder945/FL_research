def Fibonacci(num,n):
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 2):
            a = num[-1]
            b = num[-2]
            A = a + b
            num.append(A)
        return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


