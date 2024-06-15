def Fibonacci(num,n):
    a,b=1,1
    for i in range(3,n+1):
        a,b=b,a+b
        num.append(b)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


