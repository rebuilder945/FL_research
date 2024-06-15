def Fibonacci(num,  n):
    a=1
    b=1
    for i in range(0,n-2):
        c=a+b
        a=b
        b=c
    return c




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


