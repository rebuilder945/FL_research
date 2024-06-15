def Fibonacci(num,n):
    for n in range(3,n+1):
        a = num[n-1-1]+num[n-1-2]
        num.append(a)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


