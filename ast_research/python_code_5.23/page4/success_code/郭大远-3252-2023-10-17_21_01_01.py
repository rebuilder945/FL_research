def Fibonacci(num,n):
    num=[1,1]
    for i in range(n):
            s=num[-1]+num[-2]
            num.append(s)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


