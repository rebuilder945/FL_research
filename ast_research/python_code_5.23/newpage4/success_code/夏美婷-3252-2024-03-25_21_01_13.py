def Fibonacci(num,  n):
    for i in range(n-2):
        m=num[i]+num[i+1]
        num.append(m)
    return m




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


