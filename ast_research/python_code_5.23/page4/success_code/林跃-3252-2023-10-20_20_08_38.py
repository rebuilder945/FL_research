def Fibonacci(num,n):
    num=[1,1]
    for i in range(n):
        num.append(num[-1]+num[-2])
    num=num[n-1]
    return num




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


