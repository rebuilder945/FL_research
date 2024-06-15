def Fibonacci(num, n):
    i = -1
    while i < n-2:
        num.append(num[i + 1] + num[i + 2])
        i += 1
    return num[n - 1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


