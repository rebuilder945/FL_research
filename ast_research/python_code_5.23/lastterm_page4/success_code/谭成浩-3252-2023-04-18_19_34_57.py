def Fibonacci(num,n):
    for i in range(n-2):
        m[i]=num[0]+num[1]
        num[0]=num[1]
        num[1]=m[i]
    return m[i]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


