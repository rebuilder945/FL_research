def Fibonacci(n):
    if n < 2:
        return n
    a,b = 0,1
    for i in range(1,n):
        a,b = b,a+b
    return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


