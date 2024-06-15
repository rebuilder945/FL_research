def Fibonacci(a,b):
    e=0
    while b-1>1:
        e=a[1]
        a[1]=a[1]+a[0]
        b=b-1
return a[1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


