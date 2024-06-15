def Fibonacci(a,b):
    b=a
    for i in range(b):
        x=b[-1]+b[-2]
        b.append(x)
    x1=b[-1]
    return x1




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


