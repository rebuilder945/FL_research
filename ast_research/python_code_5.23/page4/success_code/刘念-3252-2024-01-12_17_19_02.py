def Fibonacci(a,b):
    while len(a)<b:
        a.append(a[-1]+a[-2])
    return a[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


