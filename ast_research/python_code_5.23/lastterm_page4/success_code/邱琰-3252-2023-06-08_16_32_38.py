def Fibonacci(num,n):
    num=[1,1]
    for i in range(1,n-1):
        num.append(num[i]+num[i-1])
    return num[n-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


