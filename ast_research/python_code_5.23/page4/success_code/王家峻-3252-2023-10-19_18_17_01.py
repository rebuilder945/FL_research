def Fibonacci(num,n):
    ls1=num.copy()
    for i in range(n+1):
        b=num[i]+num[i-1]
        num.extend(b)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


