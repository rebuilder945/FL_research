def Fibonacci(num,  n):
    n2=0
    n1=1
    c=1
    for x in range(2,n+1):
        c=n1+n2
        n2=n1
        n1=c
    return c




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


