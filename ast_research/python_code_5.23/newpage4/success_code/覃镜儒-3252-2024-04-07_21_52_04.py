def Fibonacci(num,n):
    for i in range(3,n+1):
        num.append(num[n-1-1]+num[n-1-2])
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


