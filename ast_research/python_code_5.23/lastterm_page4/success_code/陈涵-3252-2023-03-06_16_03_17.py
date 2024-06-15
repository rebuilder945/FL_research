def Fibonacci(num,n):
    a,b=num[-2],num[-1]
    for x in range(len(num)+1,n+1):
        v=a+b
        a,b=b,v
    return v  




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


