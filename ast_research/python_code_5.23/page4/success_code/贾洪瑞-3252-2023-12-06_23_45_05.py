def Fibonacci(num,n):
    if n==1 or n==2:
        return(num[0])
    else:
        for i in range(n-2):
            a=num[-2]+num[-1]
            num.append(a)
        return(num[-1])





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


