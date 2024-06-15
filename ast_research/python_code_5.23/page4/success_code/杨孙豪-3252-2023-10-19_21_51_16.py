def Fibonacci(num,n):
    a=1
    b=1
    c=a+b
    for i in range(n-2):
        a=b
        b=c
        c=a+b
    return c
        
        




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


