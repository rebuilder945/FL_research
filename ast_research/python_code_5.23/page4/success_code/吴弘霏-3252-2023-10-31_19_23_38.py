def Fibonacci(num,n):
    n1=0
    n2=1
    nows=1
    for i in range(n-1):
        nows=n1+n2
        n2=n1
        nows=n2
    return nows




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


