def Fibonacci(num,n):
    a=1
    b=1
    c=0
    for i in range(n-2):
        c=a+b
        a=b
        b=c
    return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


