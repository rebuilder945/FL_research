def Fibonacci(num,  n):
    if n>=2:
        a=1
        b=1
        for i in range(n-2):
            a=a+b
            b=a-b
        return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


