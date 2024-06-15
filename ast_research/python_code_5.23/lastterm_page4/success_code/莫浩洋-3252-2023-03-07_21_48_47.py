
def Fibonacci(num,n):
    a=1  
    b=0  
    c=1
    for i in range (n-1):
        c=a+b
        b=a
        a=c
    return c




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


