def Fibonacci(num):
    for i in range(n):
        num.append(num[len(num)]+num[len(num)+1])
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


