def Fibonacci(x,y):
    x=[1,1]
    for i in range(2,y):
        a=x[i-2]+x[i-1]
        x.append(a)
    return x[i]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


