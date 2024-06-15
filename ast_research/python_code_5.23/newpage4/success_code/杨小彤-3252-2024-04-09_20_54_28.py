def Fibonacci(num,  n):
    a = list(range(1,n+1))
    for x in a:
        num.append(num[n-1]+num[n])
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


