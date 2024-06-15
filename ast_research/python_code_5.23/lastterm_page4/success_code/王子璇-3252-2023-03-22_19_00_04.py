def Fibonacci(a,  n):
    a=[1,1]
    for x in range(1,n+1):
        a.append(a[x-1]+a[x])
    return(a[n-1])
a=[1,1]
n=int(input())
print(Fibonacci(a,n))




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


