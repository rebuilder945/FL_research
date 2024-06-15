def Fibonacci(num,n):
    i=0
    while i<=n:
        a,b=num[-1],num[-2]
        c=a+b
        num.append(c)
    t=num(n-1)
    return t




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


