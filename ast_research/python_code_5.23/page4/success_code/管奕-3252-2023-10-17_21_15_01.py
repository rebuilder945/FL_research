def Fibonacci(num,n):
    a=num[0]
    b=num[1]
    x=1
    for i in range(n):
        if i<=2:
            x=1
        else:
            x=a+b
            a=b
            b=x
    return x




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


