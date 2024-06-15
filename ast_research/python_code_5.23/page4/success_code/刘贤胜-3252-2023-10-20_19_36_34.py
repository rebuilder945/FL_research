def Fibonacci(num,  n):
    for x in range(n-2):
        b=num[-2::1]
        a=sum(b)
        num.append(a)
    return(num[-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


