def Fibonacci(num,n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        for i in range(1,n+1):
             num.append(num[-2]+num[-1])
             return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


