def Fibonacci(num,  n):
    if n<2:
        return 1
    else:
        return Fibonacci(num,  n)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


