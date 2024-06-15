def Fibonacci(a,b):
    for i in range(b):
        a.append(sum(a))
    return a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


