def Fibonaccci(num,n):
    num=[1,1]
    for i in range(2,n+1):
        num.append(num[i-2]+num[i-1])
    return num[n+1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


