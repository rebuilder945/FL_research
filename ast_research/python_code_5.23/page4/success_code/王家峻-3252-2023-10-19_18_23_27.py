def Fibonacci(num,n):
    ls1=num.copy()
    for i in range(n+1):
        b=ls1[i]+ls1[i-1]
        ls1.append(b)
        c=ls1[n-1]
        return c




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


