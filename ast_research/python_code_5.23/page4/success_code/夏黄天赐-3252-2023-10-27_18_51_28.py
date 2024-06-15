def Fibonacci(num,n):
    num=[1,1]
    for i in range(n-2):
       num.append(num[-2]+num[-1])
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


