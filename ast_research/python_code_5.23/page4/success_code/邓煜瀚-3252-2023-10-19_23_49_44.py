def Fibonacci(a,b):
    a=1
    b=1
    for i in range(3,b):
        c=a+b
        a=b
        b=c
    print(c)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


