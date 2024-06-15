def Fibonacci(num,n):
    if n==1 or n==2:
        return('1')
    else:
        a,b=1,1
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        return (c)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


