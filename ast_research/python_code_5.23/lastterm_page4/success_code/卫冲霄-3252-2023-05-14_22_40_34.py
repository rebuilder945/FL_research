def Fibonacci(num,n):
    for i in range(n):
        a=int(num[-1])+int(num[-2])
        num.append(a)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


