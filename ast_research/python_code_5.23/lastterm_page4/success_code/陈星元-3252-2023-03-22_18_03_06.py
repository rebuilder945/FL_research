def Fibonacci(num,n):
    for x in range(2,n):
        b=num[x-2]+num[x-1]
        num.append(b)
    return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


