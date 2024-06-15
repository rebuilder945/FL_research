Fibonacci(x,y):
    x=[1,1]
    for i in range(2,y):
        m=x[i-1]+x[i-2]
        x.append(m)
    return x[i]
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


