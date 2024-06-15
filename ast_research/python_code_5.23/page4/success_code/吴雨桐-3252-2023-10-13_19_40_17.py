def Fibonacci(num,  n):
    for i in range(n-2):
        ans=num[0]+num[1]
        num[0]=num[1]
        num[1]=ans
    return ans




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


