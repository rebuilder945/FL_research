def Fibonacci(num,n):
    while n>2:
        b=num[-1]+num[-2]
        num.append(b)
        n-=1
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


