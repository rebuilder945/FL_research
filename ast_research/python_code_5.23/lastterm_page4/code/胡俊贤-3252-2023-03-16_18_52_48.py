def Fibonacci(num,n)
    for i in range(n-2)
        x=num(0)+num(1)
        num(0)=num(1)
        num(1)=x
    return x
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


