def Fibonacci(num,n):
    a = 0
    b = 1
    c = 1
    for x in range(2, n+1):
        c = a+ b
        a= b
        b= c
    return c





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


