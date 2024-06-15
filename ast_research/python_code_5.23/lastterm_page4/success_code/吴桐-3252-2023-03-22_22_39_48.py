def Fibonacci(num,n):
    F=num
    for i in range(2,n):
        m=F[-1]+F[-2]
        F.append(m)
    return F[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


