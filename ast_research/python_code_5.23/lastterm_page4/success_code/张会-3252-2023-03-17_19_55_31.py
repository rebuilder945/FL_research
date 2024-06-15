def Fibonacci(num,  n):
    for i in range(n - 1):
        if i > 1:
             a = num[i] = num[i-1] + num[i-2]
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


