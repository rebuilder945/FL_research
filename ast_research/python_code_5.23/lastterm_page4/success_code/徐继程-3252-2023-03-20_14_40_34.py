def Fibonacci(a,n):
    for i in range(n-1):
        b=a[0]+a[1]
        a[0]=a[1]
        a[1]=b
    return a[0]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


