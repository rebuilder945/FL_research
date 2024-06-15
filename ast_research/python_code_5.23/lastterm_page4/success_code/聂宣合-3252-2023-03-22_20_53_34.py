def Fibonacci(num,n):
    a = 0
    b = 1
    i = 1
    while i < n:
        a,b = b,a+b
        i = i+1
    return(b) 




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


