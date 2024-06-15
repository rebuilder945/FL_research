def Fibonacci(num, n):
    if n <= len(num):
        return num[n-1]
    else:
        f = Fibonacci(num, n-1) + Fibonacci(num, n-2)
        num.append(f)
        return f





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


