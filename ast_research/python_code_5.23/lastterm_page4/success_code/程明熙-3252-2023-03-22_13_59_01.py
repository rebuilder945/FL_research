def Fibonacci(num,n):
    a=num[:1]
    b=num[1:]
    for i in range(n-1):
        a,b=b,a+b
        c=b
    return(c)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


