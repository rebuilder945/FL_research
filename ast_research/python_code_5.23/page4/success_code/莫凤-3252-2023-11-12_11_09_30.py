def Fibonacci(num,n):
    a=1
    b=1
    if n>2:
        for x in range(n-2):
            c=a+b
            a=b
            b=c
        return c
    else:
        return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


