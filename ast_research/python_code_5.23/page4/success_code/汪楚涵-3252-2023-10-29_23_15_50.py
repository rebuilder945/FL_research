def Fibonacci(num,n):
    n1=1
    n2=0
    a=1
    for x in range(2,n+1):
        a=n1+n2
        n2=n1
        n1=a
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


