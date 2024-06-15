def Fibonacci(num,n)
    for i in range(999999999):
        b=num[-1]+num[-2]
        num.append(b)
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


