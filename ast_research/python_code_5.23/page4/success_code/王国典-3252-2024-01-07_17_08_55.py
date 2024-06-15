def Fibonacci(a,b):
    for i in range(2,b):
        a.append(a[i-1]+a[i-2])
    return max(a) 




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


