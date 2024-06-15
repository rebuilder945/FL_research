def Fibonacci(num,n):
    for x in range(n-2):
        n1=num[-2]+num[-1]
        num.append(n1)
    return n1  




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


