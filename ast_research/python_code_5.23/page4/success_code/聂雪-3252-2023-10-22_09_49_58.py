def  Fibonacci(num,n):
    if n==1 or n==2:
        return 1
    elif n>=3:
        for i in range(1,n-1):
            fn = num[-1]+num[-2]
            num.append(fn)
            return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


