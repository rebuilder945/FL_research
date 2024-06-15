def Fibonacci(num,n):
    for i in range(n-2):
        num.append(num[n-3]+num[n-2])
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


