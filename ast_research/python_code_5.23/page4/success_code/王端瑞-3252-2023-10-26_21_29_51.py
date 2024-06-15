def Finonacci(num, n):
    for i in range(n-1):
        num[0],num[1] = num[1],num[0]+num[1]
    return num[0]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


