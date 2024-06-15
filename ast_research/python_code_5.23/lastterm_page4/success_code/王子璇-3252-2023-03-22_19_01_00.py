def Fibonacci(a,  b):
    a=[1,1]
    for x in range(1,b+1):
        a.append(a[x-1]+a[x])
    return(a[b-1])
a=[1,1]
n=int(input())
print(Fibonacci(a,b))




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


