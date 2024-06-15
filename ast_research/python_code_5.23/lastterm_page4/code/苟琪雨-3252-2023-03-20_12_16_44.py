def Fibnacci(num，n):
    if n <= 1:
        return num[n]
    for i in range(2,n+1):
        result.append(num[i-1]+num[i-2])
    return num[n]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


