def Fibonacci(num,n):
    a,b=num[0],num[1]
    for i in range(n-1):
        a,b=b,a+b
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


