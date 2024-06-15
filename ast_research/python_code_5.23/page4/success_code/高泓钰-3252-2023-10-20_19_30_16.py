def Fibonacci(num,n):
    for i in range(2,n+1):
        num.append(i)
        for m in range(0,len(num)):
            total+=num[m]
    return total




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


