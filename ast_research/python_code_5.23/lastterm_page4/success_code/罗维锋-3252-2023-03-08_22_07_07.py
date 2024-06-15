def Fibonacci(a,N):
    for i in range(N-2):
        a.append(a[i]+a[i+1])
    return a[N-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


