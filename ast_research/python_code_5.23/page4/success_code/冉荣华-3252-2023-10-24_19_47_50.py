def Fibonacci(n,num):
    a=1
    b=1
    for i in range(n):
        if i <2:
            fibnext=1
        else:
            fibnext=a+b
            a=b
            b=fibnext
        return fibnext




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


