def Fibonacci(num,n):   
    a=num[0]
    b=num[1]
    if n >2:
        for i in range(n-2): 
            f=a+b
            a=b
            b=f
    else:
        f=1
    return f
num=[1,1]
n=int(input())
print(Fibonacci(num,n))




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


