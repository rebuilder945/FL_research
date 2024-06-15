def Fibonacci(N):
    a=[1,1]
    if N>2:
        for i in range(N-2):
            a.append(a[i]+a[i+1])
    return a[N-1]
n=eval(input())
b=[Fibonacci(n+2)/Fibonacci(n+1) for n in range(1,n+1)]
print(b)
print("{:.4f}".format(sum(b)))
