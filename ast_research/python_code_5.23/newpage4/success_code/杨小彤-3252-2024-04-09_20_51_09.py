def Fibonacci(num,  n):
    for x in range(1,n+2):
        num.append(num[n-1]+num[n])
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


