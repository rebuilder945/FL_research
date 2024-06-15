def Fibonacci(num,n):
    if n>2:
        for i in range(3,n+1):
            Fibonacci(i)=Fibonacci(i-1)+Fibonacci(i-2)
            num.appeng(Fibonacci(i))
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


