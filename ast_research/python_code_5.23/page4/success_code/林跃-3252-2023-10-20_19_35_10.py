def Fibonacci(num,n):
    b=[1,1]
    for i in range(n-2):
        b.append(sum(num[i-1:i]))
        num=b[n-1]
        return num




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


