def Fibonacci(num,n):
    for x in num[-1]:
        for y in num[-2]:
            num.append(x+y)
            return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


