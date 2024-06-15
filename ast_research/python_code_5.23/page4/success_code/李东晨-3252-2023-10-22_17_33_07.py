def Fibonacci(num,n):
    for x in range(n):
        num+=[num[x]+num[x+1]]
    return num




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


