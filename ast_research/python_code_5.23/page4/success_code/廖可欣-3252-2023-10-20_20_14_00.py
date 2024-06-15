def Fibonacci(num,n):
    for i in range(n-2):
        a = num[i]
        b = num[i+1]
        c = a+b
        num.append(c)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


