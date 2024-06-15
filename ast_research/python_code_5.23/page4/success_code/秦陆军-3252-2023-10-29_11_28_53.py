def Fibonacci(num, n):
    while len(num) < n:
        next_value = num[-1] + num[-2]
        num.append(next_value)
    return num[n - 1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


