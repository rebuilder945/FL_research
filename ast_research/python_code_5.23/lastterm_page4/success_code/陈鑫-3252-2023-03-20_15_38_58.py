def Fibonacci(num,n):
    for x in num:
        num[-1]=num[-2]+num[-3]
        return num
    return Fibonacci[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


