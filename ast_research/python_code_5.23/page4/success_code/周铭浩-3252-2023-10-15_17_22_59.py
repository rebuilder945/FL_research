def Fibonacci(a,n):
    while True:
        b=a[-1]+a[-2]
        a.append(b)
        return a[n-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


