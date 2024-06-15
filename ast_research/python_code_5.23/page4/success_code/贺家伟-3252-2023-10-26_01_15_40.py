def Fibonacci():
    a=1
    b=1
    for i in range (n+2):
        c=a+b
        a=b
        b=c
        return c
        




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


