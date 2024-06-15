def Fibonacci(N):
    a=[2,3]
    for i in range(N-2):
        a.append(a[i]+a[i+1])
    return a[N-1]
n=eval(input())
b=[Fibonacci(n)/n for n in range(1,n+1)]
print("{:.4f}".format(sum(b)))
