def Fibonacci(num,n):
    for i in range(n-2):
        num.append(int(num[-2])+int(num[-1]))
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


