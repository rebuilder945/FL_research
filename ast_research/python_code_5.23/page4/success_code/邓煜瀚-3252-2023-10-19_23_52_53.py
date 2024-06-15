def Fibonacci(a,b):
    c=1
    d=1
    for i in range(3,b):
        e=c+d
        c=d
        d=e
    print(e)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


