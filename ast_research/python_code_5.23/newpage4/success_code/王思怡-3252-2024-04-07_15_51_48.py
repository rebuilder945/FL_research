def Fibonacci(num,n):
    a = list(range(1,n+1))
    for i in a:
         num.append(num[i]+num[i-1])
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


