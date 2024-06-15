def Fibonaci(num,n):
    x2=0
    x1=1
    num=1
    for x in range(2,n+1):
        num=x1+x2
        x2=x1
        x1=num
    return num




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


