def Fibonacci(num,n):
    a = 1
    b = 1
    c = 0
    for x in range(3,n+1):
        c = a+b
        a = b
        b = c
    return c
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


