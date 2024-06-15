def Fibonacci(num,  n):
    for i in range(n-2):
        num.append(sum(num[-1:-3:-1]))
    return num.pop()




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


