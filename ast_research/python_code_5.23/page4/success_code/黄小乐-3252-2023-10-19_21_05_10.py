def Fibonacci(num,  n):
    n=int(n)
    for i in range(n-2):
        c = num[-2]+num[-1]
        num.append(c)
    return(c)    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


