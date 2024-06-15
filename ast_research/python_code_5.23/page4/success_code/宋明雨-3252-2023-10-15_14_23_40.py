def Fibonacci(num,n):
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 2):
            A = sum(num[-1:-3])
            num.append(A)
        return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


