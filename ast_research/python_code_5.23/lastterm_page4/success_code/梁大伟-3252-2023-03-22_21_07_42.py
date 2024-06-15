def Fibonacci(num,n):
    for i in range(n-2):
        t=sum(num)
        if i % 2 == 0:
            num[0]=t
        else:
            num[1]=t
    return t




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


