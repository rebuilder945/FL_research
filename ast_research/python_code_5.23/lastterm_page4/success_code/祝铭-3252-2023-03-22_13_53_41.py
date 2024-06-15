def Fibonacci(x,y):
    pv=1
    ppv=1
    for i in range(y):
        if i<=2:
            value=1
        else:
            value=pv+ppv
            pv=ppv
            ppv=value
    return value




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


