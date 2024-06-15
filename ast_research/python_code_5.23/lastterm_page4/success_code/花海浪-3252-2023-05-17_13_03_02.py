def Fibonacci(num,n):
    for i in range(3,n+1):
        a=num[i-3]+num[i-2]
        num.append(a)
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


