def Fibonacci(a,b):
    for i in range(b):
        if i>1:
            c=a[i-1]+a[i-2]
            a.append(c)
    d=a[b-1]
    return d




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


