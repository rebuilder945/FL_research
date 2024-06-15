def Fibonacci(num,n):
    i =4
    while i <= n:
        num[0],num[1] = num[1],sum(num)
        i = i + 1
    a = sum(num)
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


