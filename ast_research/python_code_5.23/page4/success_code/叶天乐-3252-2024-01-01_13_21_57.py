def Fibonacci(num,n):
    a,b = 1,1
    for i in range(n-2):
        a,b = b,a+b
    return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


