def Fibonacci(x,y):
    while y>2:
        b=x[-1]+x[-2]
        x.append(b)
       
    return x[-1]    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


