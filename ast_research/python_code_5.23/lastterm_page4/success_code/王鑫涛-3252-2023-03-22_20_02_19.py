def Fibonacci(a,b):
    for i in range(b):
        a.append(a[-1]+a[-2])
    return a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


