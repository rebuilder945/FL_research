def Fibonacci(num,n):
    for x in range (3,n+1):
        v=num[-2]+num[-1]
        num.append(v)
    return(v)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


