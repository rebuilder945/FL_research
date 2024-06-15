def Fibonacci(num,n):
    for i in range(n-2):
        c=sum(num[-2:])
        num.append(c)
    b=num[n-1]
    return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


