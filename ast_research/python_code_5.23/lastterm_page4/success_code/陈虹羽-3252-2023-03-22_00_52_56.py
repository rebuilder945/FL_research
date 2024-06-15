def Fibonacci(x,y):
    x=[1,1]
    for i in range(2,n):
        a=x[i-2]+x[i-1]
        x.append(a)
    return x[n-1] 




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


