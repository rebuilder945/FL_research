def Fibonacci(num,n):
    for i in (3,n+1):
        a=num[i-1]+num[i-2]
        num.append(a)
    return num[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


