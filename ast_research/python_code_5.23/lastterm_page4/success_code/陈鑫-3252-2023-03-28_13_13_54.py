def Fibonacci(a,b):
    for f in range(b):
        s=a[f+1]+a[f]
        a.append(s)
    return Fibonacci[b-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


