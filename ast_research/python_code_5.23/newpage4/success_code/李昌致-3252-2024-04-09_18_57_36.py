def Fibonacci(num,n):
    num = [1,1]
    for i in range(2,n):
        a = num[-1]+num[-2]
        num.append(a)
    return a[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


