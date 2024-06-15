def Fibonacci(num,n):
    for i in range(n-2):
        k=num[-1]+num[-2]
        num.append(k)
    return k




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


