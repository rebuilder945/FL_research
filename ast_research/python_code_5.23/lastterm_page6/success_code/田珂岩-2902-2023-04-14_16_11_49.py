def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
m = 0
N = 0
s = 0
n = int(input())
while N < n:
    m = Fibonacci(N+3)/Fibonacci(N+2)
    N += 1
    s += m
print("%.4f"%s)    
    



