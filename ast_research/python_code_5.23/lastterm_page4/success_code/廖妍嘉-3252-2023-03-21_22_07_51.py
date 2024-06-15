def Fibonacci(num,  n):
    a=1
    b=1
    for i in range(n):
        if i<2:
            c=1
        else:
            c=b+a
            a=b
            b=c
    return c




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


