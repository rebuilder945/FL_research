def Fibonacci(num, n):
    if n <= len(num):
        return num[n-1]
    else:
        for i in range(len(num), n):
            num.append(num[i-1] + num[i-2])
        return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


