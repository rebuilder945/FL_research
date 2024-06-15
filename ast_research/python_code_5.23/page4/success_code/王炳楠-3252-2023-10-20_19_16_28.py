def Fibonacci(a,b):
    for i in range(b):
        a.append(a[i]+a[i+1])
    return a[b]
        




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


