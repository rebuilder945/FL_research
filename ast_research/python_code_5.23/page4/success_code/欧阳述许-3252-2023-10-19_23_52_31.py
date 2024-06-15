def Fibonacci(num,n):
    a=1
    b=1
    if n>2:
        for x in range(n-2):
            c=a+b
            a=b
            b=c
    else:
        c=1
        return c





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


