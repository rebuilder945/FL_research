def Fibonacci(num,n):
    for i in range(n-2):
        b=list(num[i:i+2])
        num=num+[sum(b)]
    a=int(num[-1])
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


