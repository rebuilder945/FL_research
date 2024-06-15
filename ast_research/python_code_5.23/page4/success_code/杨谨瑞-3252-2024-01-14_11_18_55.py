def Fibonacci(num,n):
    for i in range(100):
        su1=0
        x=num[i]+num[i+1]
        num+=[x]
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


