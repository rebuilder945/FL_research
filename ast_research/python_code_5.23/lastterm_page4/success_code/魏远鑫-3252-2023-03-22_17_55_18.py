def Fibonacci(num,  n):
    a,b=num[-2],num[-1]
    for i in range(n-2):
        a,b=b,a+b
        num.apend(b)
    return num[-1]
        




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


