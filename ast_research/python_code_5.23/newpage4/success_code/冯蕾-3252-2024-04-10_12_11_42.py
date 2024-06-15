def Fibonacci(num,  n):
    for i in range(n):
        a=num[i]+num[i+1]
        num.append(a)
    return num[n-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


