def Fibonacci(num,n):
    for x in range(3,n+1):
        num.append(num[x-1-1]+num[x-1-2])
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


