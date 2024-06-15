def Fibonacci(num,n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        for i in range(3,n+1):
             num.append(num[i-1]+num[i-2])
             return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


