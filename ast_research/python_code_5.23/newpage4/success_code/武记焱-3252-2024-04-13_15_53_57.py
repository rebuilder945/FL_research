def Fibonacc(num,n):
    for i in range(n):
        a=num[-1]+num[-2]
        num.append(a)
    n-=1
    c=num[n]
    return(c)
        





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


