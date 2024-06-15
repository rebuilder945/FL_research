def Fibonacci(num,n):
    a,b = num
    for i in range(n-2):
        c = a + b
        a = b
        b = c
    return an+1




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


