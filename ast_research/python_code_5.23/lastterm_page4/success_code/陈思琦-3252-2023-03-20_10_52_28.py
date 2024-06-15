def Fibonacci(num,n):
    for a in range(0,n-2):
        num.append(num[a]+num[a+1])
    return num[n-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


