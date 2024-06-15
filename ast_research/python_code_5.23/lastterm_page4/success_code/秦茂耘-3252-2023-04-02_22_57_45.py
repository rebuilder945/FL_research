def Fibonacci(num,  n):
    for i in range(n-2):
        num+=[num[i]+num[i+1]]
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


