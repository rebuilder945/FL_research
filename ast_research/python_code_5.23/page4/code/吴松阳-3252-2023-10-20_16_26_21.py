def Fibonacci(num,n)
    for i in range(n)
        if i > 1:
        num.append(sum(num[-2:-1]))
    a = num[n-1]
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


