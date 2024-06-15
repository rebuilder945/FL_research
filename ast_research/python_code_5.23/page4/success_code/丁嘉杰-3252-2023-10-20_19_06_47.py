def Fibonacci(num,n):
    for i in (3,n+1):
        a=num[n-1]+num[n-2]
        num.append(a)
    return num[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


