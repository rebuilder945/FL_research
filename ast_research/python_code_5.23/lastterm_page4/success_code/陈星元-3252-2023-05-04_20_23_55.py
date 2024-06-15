def Fibonacci(a,n):
    for x in range(n-2):
        b=a[x]+a[x+1]
        a.append(b)
    return a[-1]
            





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


