def Fibonacci(num,n):
    a=num
    for x in range(2,n):
        a.append(a[-2]+a[-1])
    return a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


