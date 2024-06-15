def Fibonacci(num,n):
    for x in range(n):
        y=num[x]+num[x+1]
        num.append(y)
        if x==(n-3):
            return y 

    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


