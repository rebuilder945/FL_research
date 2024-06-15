def Fibonacci(num,n):
    b=[1,1]
    for i in range(n):
        b.append(num[-1]+num[-2])
    num=b[n-1]
    return num




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


