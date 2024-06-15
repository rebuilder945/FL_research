def Fibonacci(x,y):
    for i in range(2,y):
        nu=(x[i-1]+x[i-2])
        x.append(nu)
    return x[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


