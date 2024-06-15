def Fibonacci(num,n):
    for n in range(n-2):
        m=num[-1:-3:-1]
        a=sum(m)
        num.append(a)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


