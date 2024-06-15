def Fibonacci(num,  n):
    for i in range(2,n+2):
        x=num[i-2]+num[i-1]
        num.append(x)
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


