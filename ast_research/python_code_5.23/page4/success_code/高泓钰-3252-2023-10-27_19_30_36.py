def Fibonacci(num,n):
    for i in range(n-3):
        x=num[-1]
        y=num[-2]
        m=x+y
        num.append(m)
    return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


