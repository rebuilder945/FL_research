def Fibonacci(num,n):
    for i in range(n):
        if i >= 2:
            num.append(sum(num))
    return num[n-2]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


