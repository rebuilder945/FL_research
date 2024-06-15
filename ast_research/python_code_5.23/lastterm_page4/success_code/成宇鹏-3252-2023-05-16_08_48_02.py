def Fibonacci(num,n):
    a = 0
    while a <= n-1:
        b = num[a+1] + num[a]
        num.append(b)
        a += 1
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


