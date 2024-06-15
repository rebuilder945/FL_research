def Fibonacci(num,  n):
    a = num[0]
    b= num[1]
    for i in range(n):
        c = a + b
        a = b
        b = c
        num.append(c)
    d = num[n-1]
    return d




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


