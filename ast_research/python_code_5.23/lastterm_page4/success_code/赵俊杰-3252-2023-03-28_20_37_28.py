def Fibonacci(num,n):
    while n>2:
        num.append(num[-1]+num[-2])
        n=n-1
    return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


