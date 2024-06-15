def Fibonacci(num,n):
    for i in range(n-2):
        a=num[i]+num[i+1]
        num.append(a)
        b=num[-1]
        return(b)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


