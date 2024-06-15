def Fibonacci(num,n):
    for i in range(8):
        a=num[-1]+num[-2]
        num.append(a)
    return(num[n])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


