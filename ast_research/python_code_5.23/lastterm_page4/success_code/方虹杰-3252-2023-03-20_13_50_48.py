def Fibonacci(num,  n):
    for i in range(2,n+1):
        num.append([i-1]+[i-2])
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


