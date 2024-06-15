def Fibonacci(num):
    a,b=0,1
    for i in range(num):
        a,b=b,a+b
    return a





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


