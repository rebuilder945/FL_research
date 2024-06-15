def Fibonacci(a,x1):
    x3=x1-2
    b=a
    for i in range(x3):
        x=b[-1]+b[-2]
        b.append(x)
    x1=b[-1]
    return x1
num=[1,1]
n=int(input())
print(Fibonacci(num,n))




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


