def Fibonacci(num,n):
    dnx = 0
    if n <= 2:
        return(1)
    else:
        for i in range(1,n-1):
            fn = num[-1] + num[-2]
            num.append(fn)
        return(num[-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


