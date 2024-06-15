def Fibonacci(num, n):
    for i in range(2, n):
        sum = num[i-2] + num[i-1]
        num.append(sum)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


