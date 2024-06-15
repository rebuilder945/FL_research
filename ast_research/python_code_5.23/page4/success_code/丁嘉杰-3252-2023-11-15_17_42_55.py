def Fibonacci(num,n):
    last=num[0]
    now=num[1]
    fibnext=1
    for i in range(n):
        while n >2:
            fibnext=last+now
            last=now
            now=fibnext
            n-=1
        return fibnext




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


