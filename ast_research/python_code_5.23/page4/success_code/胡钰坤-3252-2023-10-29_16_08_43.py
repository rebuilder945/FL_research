def Fibonacci(x,y):
    for i in range(y-2):
        z = x[-2]+x[-1]
        x.append(z)
    return z




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


