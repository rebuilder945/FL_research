def Fibonacci(num,n):
    last=num[0]
    now=num[1]
    fibnext=1
    for i in range(n):
        if i >=2:
            fibnext2=last+now
            last=now
            now=fibnext2
        return fibnext2




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


