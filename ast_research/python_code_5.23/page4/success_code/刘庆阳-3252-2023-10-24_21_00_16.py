def Fibonacci(num,n):
    while n > 2:
        n -=1
        a = int(num[-1]) + int(num[-2])
        num.append(a)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


