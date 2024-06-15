def Fibonacci(num,n):
    for i in range(n-2):
        sum1 = num[-1]+num[-2]
        num.append(sum1)
    x = num[n-1]
    return x




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


