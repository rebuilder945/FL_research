def Fibonacci(num,n):
    for i in range(n):
        a=num[i]+num[i+1]
        num.append(a)
        if (i+1)==(n-2):
            return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


