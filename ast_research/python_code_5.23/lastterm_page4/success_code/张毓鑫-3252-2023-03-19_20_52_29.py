def Fibonacci(num,n):
    if n>len(num):
        for i in range(len(num)):
            a=num[-1]+num[-2]
            num.appen(a)
    return




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


