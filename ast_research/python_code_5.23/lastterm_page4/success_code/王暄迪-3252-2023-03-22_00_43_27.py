def Fibonacci(num,n):
    s=n-2
    for i in range(s):
        a=int(num[-2])
        b=int(num[-1])
        c=a+b
        num.append(c)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


