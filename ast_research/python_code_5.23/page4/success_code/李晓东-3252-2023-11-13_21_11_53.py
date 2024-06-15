def Fibonacci(num,n):
    for x in range(3,n+1):
        a = num[x-1]+num[x-2]
        num.append(a)
    b = num[n-1]
    return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


